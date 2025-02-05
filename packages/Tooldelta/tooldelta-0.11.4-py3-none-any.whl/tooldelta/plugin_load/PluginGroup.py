"插件加载器框架"

import asyncio
import os
import traceback
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, ClassVar, TypeVar

from ..color_print import Print
from ..constants import (
    TOOLDELTA_CLASSIC_PLUGIN,
    TOOLDELTA_INJECTED_PLUGIN,
    TOOLDELTA_PLUGIN_DIR,
    PacketIDS,
    SysStatus,
)
from ..game_utils import _set_frame
from ..plugin_load import (
    NON_FUNC,
    PluginAPINotFoundError,
    PluginAPIVersionError,
    auto_move_plugin_dir,
)
from ..utils import Utils
from .classic_plugin import (
    _PLUGIN_CLS_TYPE,
    Plugin,
    _init_frame,
    add_plugin,
    add_plugin_as_api,
)
from . import classic_plugin
from . import injected_plugin
from . import _ON_ERROR_CB

if TYPE_CHECKING:
    from ..frame import ToolDelta

_TV = TypeVar("_TV")
_SUPER_CLS = TypeVar("_SUPER_CLS")

# add_plugin(): 类式插件调用, 插件框架会将其缓存到自身缓存区, 等待类式插件将插件类实例化
# add_broadcast_listener(), add_packet_listener() 同理
# 对于使用了 add_plugin_as_api() 的插件, 可以使用 get_plugin_api() 跨插件获取接口


class PluginGroup:
    "插件组类, 存放插件代码有关数据"

    Agree_bot_patrol: ClassVar["list[bool]"] = []

    def __init__(self):
        "初始化"
        # loaded_plugin_ids: 供给插件调用
        self._cached_broadcast_evts: dict[str, list[Callable]] = {}
        self._cached_packet_cbs: list[tuple[int, Callable]] = []
        self._cached_all_packets_listener: Callable | None = None
        self._update_player_attributes_funcs: list[Callable] = []
        self._broadcast_listeners: dict[str, list[Callable]] = {}
        self.plugins_api: dict[str, Plugin] = {}
        self.normal_plugin_loaded_num = 0
        self.injected_plugin_loaded_num = 0
        self.loaded_plugin_ids = []
        self.linked_frame: "ToolDelta | None" = None

    def reload(self):
        """
        重载插件框架
        这是一个不很安全的操作, 多次 reload 后
        可能会因为一些插件线程由于底层原因无法被停止, 或者有垃圾无法被回收, 导致内存泄露等问题
        """
        self.plugins_api = {}
        self._update_player_attributes_funcs = []
        self._broadcast_listeners = {}
        self.execute_frame_exit(SysStatus.NORMAL_EXIT, "normal")
        classic_plugin.reload()
        injected_plugin.reload()
        Print.print_inf("正在重新读取所有插件")
        self.read_all_plugins()
        assert self.linked_frame is not None
        self.execute_reloaded(self.linked_frame.on_plugin_err)
        Print.print_inf("开始执行插件游戏初始化方法")
        self.execute_init()
        Print.print_suc("重载插件已完成")

    @staticmethod
    def add_plugin(plugin: type[_PLUGIN_CLS_TYPE]) -> type[_PLUGIN_CLS_TYPE]:
        """
        添加ToolDelta类式插件的插件主类

        Args:
            plugin (type[Plugin]): 插件主类

        Raises:
            NotValidPluginError: 插件主类必须继承 Plugin 类

        Returns:
            type[Plugin]: 插件主类
        """
        return add_plugin(plugin)

    @staticmethod
    def add_plugin_as_api(apiName: str):
        """
        添加 ToolDelta 类式插件主类，同时作为 API 插件提供接口供其他插件进行使用

        Args:
            apiName (str): API 名
        """
        return add_plugin_as_api(apiName)

    def add_packet_listener(self, pktID: int | list[int]):
        """
        添加数据包监听器
        将下面的方法作为一个 MC 数据包接收器
        Tips: 只能在插件主类里的函数使用此装饰器!

        Args:
            pktID (int | list[int]): 数据包 ID 或多个 ID

        Returns:
            Callable[[Callable], Callable]: 添加数据包监听器
        """

        def deco(func: Callable[[_SUPER_CLS, dict], bool]):
            # 存在缓存区, 等待 class_plugin 实例化
            if pktID == -1:
                for n, i in PacketIDS.__dict__.items():
                    if n[0].isupper():
                        self._cached_packet_cbs.append((i, func))
            elif isinstance(pktID, int):
                self._cached_packet_cbs.append((pktID, func))
            else:
                for i in pktID:
                    self._cached_packet_cbs.append((i, func))
            return func

        return deco

    def add_any_packet_listener(self, func: Callable[[_SUPER_CLS, int, dict], bool]):
        """
        添加任意数据包监听器, 供插件开发 Debug 使用
        注意: 由于 Python JSON 解析速度过慢, 此方法很有可能降低整体运行速度!
        Tips: 只能在插件主类里的函数使用此装饰器!

        Returns:
            Receiver ((pktID: int, pkt: dict) -> bool): 数据包监听器接收器, 传入 数据包ID, 数据包 返回 bool
        """
        self._cached_all_packets_listener = func
        return func

    def add_broadcast_listener(self, evt_name: str):
        """
        添加广播事件监听器
        将下面的方法作为一个广播事件接收器
        Tips: 只能在插件主类里的函数使用此装饰器!

        Args:
            evt_name (str): 事件名

        Returns:
            Callable[[Callable], Callable]: 添加广播事件监听器

        原理:
        方法 1 广播：hi, what's ur name? 附加参数=english_only
            - 方法 2 接收到广播并被执行：方法 2(english_only) -> my name is Super. -> 收集表

        事件 1 获取到 收集表 作为返回：["my name is Super."]
        """

        def deco(
            func: Callable[[_SUPER_CLS, _TV], Any],
        ) -> Callable[[_SUPER_CLS, _TV], Any]:
            # 存在缓存区, 等待 class_plugin 实例化
            if self._cached_broadcast_evts.get(evt_name):
                self._cached_broadcast_evts[evt_name].append(func)
            else:
                self._cached_broadcast_evts[evt_name] = [func]
            return func

        return deco

    def broadcastEvt(self, evt_name: str, data: Any = None) -> list[Any]:
        """
        向全局广播一个特定事件，可以传入附加信息参数
        Args:
            evt_name (str): 事件名
            data (Any, optional): 附加信息参数
        Returns:
             list[Any]: 收集到的数据的列表 (如果接收到广播的方法返回了数据的话)
        """
        callback_list = []
        res = self._broadcast_listeners.get(evt_name)
        if res:
            for f in res:
                res2 = f(data)
                if res2:
                    callback_list.append(res2)
        return callback_list

    @staticmethod
    def help(plugin: Plugin) -> None:
        """
        查看插件帮助.
        常用于查看 get_plugin_api() 方法获取到的插件实例的帮助.
        """
        plugin_docs = "<plugins.help>: " + plugin.name + "开放的 API 接口说明:\n"
        for attr_name, attr in plugin.__dict__.items():
            if not attr_name.startswith("__") and attr.__doc__ is not None:
                plugin_docs += (
                    "\n §a"
                    + attr_name
                    + ":§f\n    "
                    + attr.__doc__.replace("\n", "\n    ")
                )
        Print.clean_print(plugin_docs)

    def checkSystemVersion(self, need_vers: tuple[int, int, int]):
        """检查 ToolDelta 系统的版本

        Args:
            need_vers (tuple[int, int, int]): 需要的版本

        Raises:
            self.linked_frame.SystemVersionException: 该组件需要的 ToolDelta 系统版本
        """
        if (
            self.linked_frame is not None
            and need_vers > self.linked_frame.sys_data.system_version
        ):
            raise self.linked_frame.SystemVersionException(
                f"该插件需要ToolDelta为最低 {'.'.join([str(i) for i in self.linked_frame.sys_data.system_version])} 版本，请及时更新"
            )
        if self.linked_frame is None:
            raise ValueError(
                "无法检查 ToolDelta 系统版本，请确保已经加载了 ToolDelta 系统组件"
            )

    def get_plugin_api(
        self, apiName: str, min_version: tuple | None = None, force=True
    ) -> Any:
        """获取插件 API

        Args:
            apiName (str): 插件 API 名
            min_version (tuple | None, optional): API 最低版本 (若不填则默认不检查最低版本)
            force: 若为 False, 则在找不到插件 API 时不报错而是返回 None

        Raises:
            PluginAPIVersionError: 插件 API 版本错误
            PluginAPINotFoundError: 无法找到 API 插件

        Returns:
            Plugin: 插件 API
        """
        api = self.plugins_api.get(apiName)
        if api:
            if min_version and api.version < min_version:
                raise PluginAPIVersionError(apiName, min_version, api.version)
            return api
        if force:
            raise PluginAPINotFoundError(apiName)
        return None

    def set_frame(self, frame: "ToolDelta") -> None:
        """为各个框架分发关联的系统框架"""
        self.linked_frame = frame
        _set_frame(frame)
        _init_frame(frame)

    def read_all_plugins(self) -> None:
        """
        读取所有插件/重载所有插件 并对插件进行预初始化

        Raises:
            SystemExit: 读取插件出现问题
        """
        if self.linked_frame is None or self.linked_frame.on_plugin_err is None:
            raise ValueError("无法读取插件，请确保系统已初始化")
        for fdir in os.listdir(TOOLDELTA_PLUGIN_DIR):
            if fdir not in (TOOLDELTA_CLASSIC_PLUGIN, TOOLDELTA_INJECTED_PLUGIN):
                auto_move_plugin_dir(fdir)
        self.loaded_plugin_ids = []
        self.normal_plugin_loaded_num = 0
        self.injected_plugin_loaded_num = 0
        try:
            Print.print_inf("§a正在使用 §bHiQuality §dDX§r§a 模式读取插件")
            classic_plugin.read_plugins(self)
            asyncio.run(injected_plugin.load_plugin(self))
            # 主动读取类式插件监听的数据包
            for i in classic_plugin.packet_funcs.keys():
                self.__add_listen_packet_id(i)
            # 主动读取类式插件监听的广播事件器
            self._broadcast_listeners.update(classic_plugin.broadcast_evts_listener)
            # 主动读取注入式插件监听的数据包
            for i in injected_plugin.packet_funcs.keys():
                self.__add_listen_packet_id(i)
            # 因为注入式插件自带一个handler, 所以不用再注入方法
            Print.print_suc("所有插件读取完毕, 将进行插件初始化")
            self.execute_def(self.linked_frame.on_plugin_err)
            Print.print_suc(
                f"插件初始化成功, 载入 §f{self.normal_plugin_loaded_num}§a 个类式插件, §f{self.injected_plugin_loaded_num}§a 个注入式插件"
            )
        except Exception as err:
            err_str = "\n".join(traceback.format_exc().split("\n")[1:])
            Print.print_err(f"加载插件出现问题：\n{err_str}")
            raise SystemExit from err

    def __add_listen_packet_id(self, packetType: int) -> None:
        """添加数据包监听，仅在系统内部使用

        Args:
            packetType (int): 数据包 ID

        Raises:
            ValueError: 无法添加数据包监听，请确保已经加载了系统组件
        """
        if self.linked_frame is None:
            raise ValueError("无法添加数据包监听，请确保已经加载了系统组件")
        self.linked_frame.link_game_ctrl.add_listen_packet(packetType)

    def instant_plugin_api(self, api_cls: type[_PLUGIN_CLS_TYPE]) -> _PLUGIN_CLS_TYPE:
        """
        对外源导入 (import) 的 API 插件类进行类型实例化。
        可以使得你所使用的 IDE 对导入的插件 API 类进行识别和高亮其所含方法。

        Args:
            api_cls (type[_PLUGIN_CLS_TYPE]): 导入的 API 插件类

        Raises:
            ValueError: API 插件类未被注册

        Returns:
            _PLUGIN_CLS_TYPE: API 插件实例

        使用方法如下:
        ```python
            p_api = plugins.get_plugin_api("...")
            from outer_api import api_cls_xx
            p_api = plugins.instant_plugin_api(api_cls_xx)
        ```
        """
        for v in self.plugins_api.values():
            if isinstance(v, api_cls):
                return v
        raise ValueError(f"无法找到 API 插件类 {api_cls.__name__}, 有可能是还没有注册")

    def _add_listen_update_player_attributes_func(self, func: Callable) -> None:
        """添加玩家属性更新监听器，仅在系统内部使用

        Args:
            func (Callable): 数据包监听器
        """
        self._update_player_attributes_funcs.append(func)

    def execute_def(self, onerr: _ON_ERROR_CB = NON_FUNC) -> None:
        """执行插件的二次初始化方法

        Args:
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法。Defaults to NON_FUNC.

        Raises:
            SystemExit: 缺少前置
            SystemExit: 前置版本过低
        """
        classic_plugin.execute_def(onerr)

    def execute_init(self, onerr: _ON_ERROR_CB = NON_FUNC) -> None:
        """执行插件的连接游戏后初始化方法

        Args:
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法
        """
        classic_plugin.execute_init(onerr)
        asyncio.run(injected_plugin.execute_init())
        Utils.createThread(
            asyncio.run, (injected_plugin.execute_repeat(),), "注入式插件定时任务"
        )

    def execute_player_prejoin(self, player, onerr: _ON_ERROR_CB = NON_FUNC) -> None:
        """执行玩家加入前的方法

        Args:
            player (_type_): 玩家
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法
        """
        classic_plugin.execute_player_prejoin(player, onerr)
        asyncio.run(injected_plugin.execute_player_prejoin(player))

    def execute_player_join(self, player: str, onerr: _ON_ERROR_CB = NON_FUNC) -> None:
        """执行玩家加入的方法

        Args:
            player (str): 玩家
            onerr (Callable[[str, Exception, str], None], optional): q 插件出错时的处理方法
        """
        classic_plugin.execute_player_join(player, onerr)
        asyncio.run(injected_plugin.execute_player_join(player))

    def execute_player_message(
        self,
        player: str,
        msg: str,
        onerr: _ON_ERROR_CB = NON_FUNC,
    ) -> None:
        """执行玩家消息的方法

        Args:
            player (str): 玩家
            msg (str): 消息
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法
        """
        pat = f"[{player}] "
        if msg.startswith(pat):
            msg = msg.strip(pat)
        classic_plugin.execute_player_message(player, msg, onerr)
        asyncio.run(injected_plugin.execute_player_message(player, msg))

    def execute_player_leave(self, player: str, onerr: _ON_ERROR_CB = NON_FUNC) -> None:
        """执行玩家离开的方法

        Args:
            player (str): 玩家
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法
        """
        classic_plugin.execute_player_leave(player, onerr)
        asyncio.run(injected_plugin.execute_player_left(player))

    def execute_player_death(
        self,
        player: str,
        killer: str | None,
        msg: str,
        onerr: _ON_ERROR_CB = NON_FUNC,
    ):
        """执行玩家死亡的方法

        Args:
            player (str): 玩家
            killer (str | None): 击杀者
            msg (str): 击杀消息
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法
        """
        classic_plugin.execute_player_death(player, killer, msg, onerr)
        asyncio.run(injected_plugin.execute_death_message(player, killer, msg))

    def execute_frame_exit(
        self, signal: int, reason: str, onerr: _ON_ERROR_CB = NON_FUNC
    ):
        """执行框架退出的方法

        Args:
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法
        """
        classic_plugin.execute_frame_exit(signal, reason, onerr)
        asyncio.run(injected_plugin.execute_frame_exit())

    def execute_reloaded(self, onerr: _ON_ERROR_CB = NON_FUNC):
        """执行插件重载的方法

        Args:
            onerr (Callable[[str, Exception, str], None], optional): 插件出错时的处理方法
        """
        classic_plugin.execute_reloaded(onerr)
        asyncio.run(injected_plugin.execute_reloaded())

    def processPacketFunc(
        self, pktID: int, pkt: dict, onerr: _ON_ERROR_CB = NON_FUNC
    ) -> bool:
        """处理数据包监听器

        Args:
            pktID (int): 数据包 ID
            pkt (dict): 数据包

        Returns:
            bool: 是否处理成功
        """
        blocking = classic_plugin.execute_packet_funcs(pktID, pkt, onerr)
        asyncio.run(injected_plugin.execute_packet_funcs(pktID, pkt))
        return blocking


plugin_group = PluginGroup()
