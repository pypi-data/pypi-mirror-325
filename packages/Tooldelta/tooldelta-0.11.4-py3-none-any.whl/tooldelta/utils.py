"""提供了一些实用方法的类"""

import copy
import ctypes
import json
import os
import re
import threading
import time
import traceback
import shelve
from io import TextIOWrapper
from typing import Any, TypeVar, Callable  # noqa: UP035

import json

from .color_print import Print
from .constants import TOOLDELTA_PLUGIN_DATA_DIR

event_pool: dict[str, threading.Event] = {}
threads_list: list["Utils.createThread"] = []
timer_events_table: dict[int, list[tuple[str, Callable, tuple, dict, int]]] = {}
_timer_event_lock = threading.Lock()

VT = TypeVar("VT")
FACTORY_TYPE = TypeVar("FACTORY_TYPE")

MC_COLOR_CODE_REG = re.compile("§.")


class Utils:
    """提供了一些实用方法的类"""

    class ThreadExit(SystemExit):
        """线程退出."""

    class ToolDeltaThread(threading.Thread):
        """简化 ToolDelta 子线程创建的 threading.Thread 的子类."""

        SYSTEM = 0
        PLUGIN = 1
        PLUGIN_LOADER = 2

        def __init__(
            self,
            func: Callable,
            args: tuple = (),
            usage="",
            thread_level=PLUGIN,
            **kwargs,
        ):
            """新建一个 ToolDelta 子线程

            Args:
                func (Callable): 线程方法
                args (tuple, optional): 方法的参数项
                usage (str, optional): 线程的用途说明
                thread_level: 线程权限等级
                kwargs (dict, optional): 方法的关键词参数项
            """
            super().__init__(target=func)
            self.func = func
            self.daemon = True
            self.all_args = [args, kwargs]
            self.usage = usage or f"fn:{func.__name__}"
            self.start()
            self.stopping = False
            self._thread_level = thread_level

        def run(self) -> None:
            """线程运行方法"""
            threads_list.append(self)
            try:
                self.func(*self.all_args[0], **self.all_args[1])
            except (SystemExit, Utils.ThreadExit):
                pass
            except ValueError as e:
                if str(e) != "未连接到游戏":
                    Print.print_err(
                        f"线程 {self.usage or self.func.__name__} 出错:\n"
                        + traceback.format_exc()
                    )
                else:
                    Print.print_war(f"线程 {self.usage} 因游戏断开连接被迫中断")
            except Exception:
                Print.print_err(
                    f"线程 {self.usage or self.func.__name__} 出错:\n"
                    + traceback.format_exc()
                )
            finally:
                threads_list.remove(self)
                del self.all_args

        def stop(self) -> bool:
            """终止线程 注意: 不适合在有长时间sleep的线程内调用"""
            self.stopping = True
            thread_id = self.ident
            if thread_id is None:
                return True
            if not self.is_alive():
                return True
            # 也许不会出现问题了吧
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
                ctypes.c_long(thread_id), ctypes.py_object(Utils.ThreadExit)
            )
            if res == 0:
                Print.print_err(f"§c线程ID {thread_id} 不存在")
                return False
            elif res > 1:
                # 线程修改出问题了? 终止了奇怪的线程?
                # 回退修改
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, None)
                Print.print_err(f"§c终止线程 {self.name} 失败")
                return False
            return True

    # class ToolDeltaThread:
    #     """使用 start_new_thread"""

    #     SYSTEM = 0
    #     PLUGIN = 1
    #     PLUGIN_LOADER = 2

    #     def __init__(
    #         self,
    #         func: Callable,
    #         args: tuple = (),
    #         usage="",
    #         thread_level=PLUGIN,
    #         **kwargs,
    #     ):
    #         """新建一个 ToolDelta 子线程

    #         Args:
    #             func (Callable): 线程方法
    #             args (tuple, optional): 方法的参数项
    #             usage (str, optional): 线程的用途说明
    #             thread_level: 线程权限等级
    #             kwargs (dict, optional): 方法的关键词参数项
    #         """
    #         self.func = func
    #         self.args = args
    #         self.usage = usage
    #         self.start_event = threading.Event()
    #         self._thread_level = thread_level
    #         self._thread_id = _thread.start_new_thread(self.run, (), kwargs)
    #         self.start_event.wait()

    #     def run(self) -> None:
    #         """线程运行方法"""
    #         actives_dic = threading._active  # type: ignore
    #         threads_list.append(self)
    #         this_thread = actives_dic[self._thread_id]
    #         this_thread.name = f"ToolDelta 线程: {self.usage}"
    #         self.start_event.set()
    #         try:
    #             self.func(*self.args)
    #         except (SystemExit, Utils.ThreadExit):
    #             pass
    #         except ValueError as e:
    #             if str(e) != "未连接到游戏":
    #                 Print.print_err(
    #                     f"线程 {self.usage or self.func.__name__} 出错:\n"
    #                     + traceback.format_exc()
    #                 )
    #             else:
    #                 Print.print_war(f"线程 {self.usage} 因游戏断开连接被迫中断")
    #         except Exception:
    #             Print.print_err(
    #                 f"线程 {self.usage or self.func.__name__} 出错:\n"
    #                 + traceback.format_exc()
    #             )
    #         finally:
    #             threads_list.remove(self)
    #             if self._thread_id not in actives_dic.keys():
    #                 Print.print_war(f"无法从线程池移除线程: {self._thread_id}")
    #             else:
    #                 del actives_dic[self._thread_id]  # type: ignore

    #     def stop(self) -> bool:
    #         """终止线程 注意: 不适合在有长时间sleep的线程内调用"""
    #         self.stopping = True
    #         thread_id = self._thread_id or _thread.get_ident()
    #         # 也许不会出现问题了吧
    #         res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
    #             ctypes.c_long(thread_id), ctypes.py_object(Utils.ThreadExit)
    #         )
    #         if res == 0:
    #             Print.print_err(f"§c线程ID {thread_id} 不存在")
    #             return False
    #         elif res > 1:
    #             # 线程修改出问题了? 终止了奇怪的线程?
    #             # 回退修改
    #             ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, None)
    #             Print.print_err(f"§c终止线程 {self.func.__name__} 失败")
    #             return False
    #         return True

    createThread = ToolDeltaThread

    class DB:
        @staticmethod
        def open(fp: str):
            shelf = shelve.open(fp, writeback=True)
            shelvePathTmp[fp] = shelf
            return shelf

        @staticmethod
        def flush(fp: str):
            if shelvePathTmp.get(fp) is None:
                raise ValueError("数据库文件未打开")
            shelvePathTmp[fp].sync()

    class TMPJson:
        """提供了加载、卸载、读取和写入 JSON 文件到缓存区的方法的类."""

        @staticmethod
        def loadPathJson(path: str, needFileExists: bool = True) -> None:
            """
            将 json 文件从磁盘加载到缓存区，以便快速读写.
            在缓存文件已加载的情况下，再使用一次该方法不会有任何作用.

            Args:
                path (str): 作为文件的磁盘内路径的同时也会作为在缓存区的虚拟路径
                needFileExists (bool, optional): 默认为 True, 为 False 时，若文件路径不存在，就会自动创建一个文件，且默认值为 null

            Raises:
                err: 文件不存在时
            """
            if path in jsonPathTmp:
                return
            try:
                with open(path, encoding="utf-8") as file:
                    js = Utils.SimpleJsonDataReader.SafeJsonLoad(file)
            except FileNotFoundError as err:
                if not needFileExists:
                    js = None
                else:
                    raise err from None
            except UnicodeDecodeError:
                Print.print_err(path)
                raise
            jsonPathTmp[path] = [False, js]

        @staticmethod
        def unloadPathJson(path: str) -> bool:
            """
            将 json 文件从缓存区卸载 (保存内容到磁盘), 之后不能再在缓存区对这个文件进行读写.
            在缓存文件已卸载的情况下，再使用一次该方法不会有任何作用，但是可以通过其返回的值来知道存盘有没有成功.

            Args:
                path (str): 文件的虚拟路径

            Returns:
                bool: 存盘是否成功
            """
            if jsonPathTmp.get(path) is not None:
                isChanged, dat = jsonPathTmp[path]
                if isChanged:
                    with open(path, "w", encoding="utf-8") as file:
                        Utils.SimpleJsonDataReader.SafeJsonDump(dat, file)
                del jsonPathTmp[path]
                return True
            return False

        @staticmethod
        def read(path: str) -> Any:
            """对缓存区的该虚拟路径的文件进行读操作，返回一个深拷贝的 JSON 对象

            Args:
                path (str): 文件的虚拟路径

            Raises:
                Exception: json 路径未初始化，不能进行读取和写入操作

            Returns:
                list[Any] | dict[Any, Any] | Any: 该虚拟路径的 JSON
            """
            if path in jsonPathTmp:
                val = jsonPathTmp.get(path)
                if val is not None:
                    val = val[1]
                    if isinstance(val, list | dict):
                        val = copy.deepcopy(val)
                    return val
            raise ValueError("json 路径未初始化，不能进行读取和写入操作：" + path)

        @staticmethod
        def get(path: str) -> Any:
            """
            直接获取缓存区的该虚拟路径的 JSON, 不使用 copy
            WARNING: 如果你不知道有什么后果，请老老实实使用`read(...)`而不是`get(...)`!

            Args:
                path (str): 文件的虚拟路径
            """
            if path in jsonPathTmp:
                val = jsonPathTmp.get(path)
                if val is not None:
                    val = val[1]
                    return val
            raise ValueError("json 路径未初始化，不能进行读取和写入操作：" + path)

        @staticmethod
        def write(path: str, obj: Any) -> None:
            """
            对缓存区的该虚拟路径的文件进行写操作，这将会覆盖之前的内容

            Args:
                path (str): 文件的虚拟路径
                obj (Any): 任何合法的 JSON 类型 例如 dict/list/str/bool/int/float
            """
            if path in jsonPathTmp:
                jsonPathTmp[path] = [True, obj]
            else:
                raise ValueError("json 路径未初始化，不能进行读取和写入操作：" + path)

        @staticmethod
        def read_as_tmp(
            path: str,
            needFileExists: bool = True,
            timeout: int = 60,
            default: Callable[[], Any] | Any = None,
        ) -> Any:
            """读取 json 文件并将其从磁盘加载到缓存区，以便一段时间内能快速读写.

            Args:
                path (str): 作为文件的磁盘内路径的同时也会作为在缓存区的虚拟路径
                needFileExists (bool, optional): 默认为 True, 为 False 时，若文件路径不存在，就会自动创建一个文件，且写入默认值 null
                timeout (int, optional): 多久没有再进行读取操作时卸载缓存

            Returns:
                Any: 该虚拟路径的 JSON
            """
            if path not in jsonPathTmp.keys():
                if path not in jsonUnloadPathTmp.keys():
                    jsonUnloadPathTmp[path] = timeout + int(time.time())
                Utils.TMPJson.loadPathJson(path, needFileExists)
            return Utils.TMPJson.read(path) or (
                default() if callable(default) else default
            )

        @staticmethod
        def write_as_tmp(
            path: str, obj: Any, needFileExists: bool = True, timeout: int = 60
        ) -> None:
            """写入 json 文件并将其从磁盘加载到缓存区，以便一段时间内能快速读写.

            Args:
                path (str): 作为文件的磁盘内路径的同时也会作为在缓存区的虚拟路径
                obj (Any): 任何合法的 JSON 类型 例如 dict/list/str/bool/int/float
                needFileExists (bool, optional): 默认为 True, 为 False 时，若文件路径不存在，就会自动创建一个文件，且写入默认值 null
                timeout (int, optional): 多久没有再进行读取操作时卸载缓存
            """
            if path not in jsonPathTmp.keys():
                if path not in jsonUnloadPathTmp.keys():
                    jsonUnloadPathTmp[path] = timeout + int(time.time())
                Utils.TMPJson.loadPathJson(path, needFileExists)
            Utils.TMPJson.write(path, obj)

        @staticmethod
        def cancel_change(path: str) -> None:
            """取消缓存 json 所做的更改，非必要情况请勿调用，你不知道什么时候会自动保存所做更改"""
            jsonPathTmp[path][0] = False

        @staticmethod
        def flush(fp: str | None = None):
            """
            刷新单个/全部JSON缓存区的缓存文件, 存入磁盘

            Args:
                fp (str | None, optional): 文件虚拟路径
            """
            _tmpjson_save(fp)

        @staticmethod
        def get_tmps() -> dict:
            """不要调用!"""
            return jsonPathTmp.copy()

    class JsonIO:
        """提供了安全的 JSON 文件操作方法的类."""

        @staticmethod
        def SafeJsonDump(obj: Any, fp: TextIOWrapper | str, indent=2) -> None:
            """将一个 json 对象写入一个文件，会自动关闭文件读写接口.

            Args:
                obj (str | dict | list): JSON 对象
                fp (Any): open(...) 打开的文件读写口 或 文件路径
            """
            if isinstance(fp, str):
                with open(fp, "w", encoding="utf-8") as file:
                    file.write(json.dumps(obj, indent=indent, ensure_ascii=False))
            else:
                with fp:
                    fp.write(json.dumps(obj, indent=indent, ensure_ascii=False))

        @staticmethod
        def SafeJsonLoad(fp: TextIOWrapper | str) -> Any:
            """从一个文件读取 json 对象，会自动关闭文件读写接口.

            Args:
                fp (TextIOWrapper | str): open(...) 打开的文件读写口 或文件路径

            Returns:
                dict | list: JSON 对象
            """
            if isinstance(fp, str):
                with open(fp, encoding="utf-8") as file:
                    return json.load(file)
            with fp as file:
                return json.load(file)

        class DataReadError(json.JSONDecodeError):
            """读取数据时发生错误"""

        @staticmethod
        def readFileFrom(
            plugin_name: str, file: str, default: dict | None = None
        ) -> Any:
            """从插件数据文件夹读取一个 json 文件，会自动创建文件夹和文件.

            Args:
                plugin_name (str): 插件名
                file (str): 文件名
                default (dict, optional): 默认值，若文件不存在则会写入这个默认值

            Raises:
                Utils.JsonIO.DataReadError: 读取数据时发生错误
                err: 读取文件路径时发生错误

            Returns:
                dict | list: JSON 对象
            """
            if file.endswith(".json"):
                file = file[:-5]
            filepath = os.path.join(
                TOOLDELTA_PLUGIN_DATA_DIR, plugin_name, f"{file}.json"
            )
            os.makedirs(
                os.path.join(TOOLDELTA_PLUGIN_DATA_DIR, plugin_name), exist_ok=True
            )
            try:
                if default is not None and not os.path.isfile(filepath):
                    with open(filepath, "w") as f:
                        Utils.JsonIO.SafeJsonDump(default, f)
                    return default
                with open(filepath, encoding="utf-8") as f:
                    res = Utils.JsonIO.SafeJsonLoad(f)
                return res
            except json.JSONDecodeError as err:
                # 判断是否有 msg.doc.pos 属性
                raise Utils.JsonIO.DataReadError(err.msg, err.doc, err.pos)
            except Exception as err:
                Print.print_err(f"读文件路径 {filepath} 发生错误")
                raise err

        @staticmethod
        def writeFileTo(plugin_name: str, file: str, obj: Any, indent=4) -> None:
            """将一个 json 对象写入插件数据文件夹，会自动创建文件夹和文件.

            Args:
                plugin_name (str): 插件名
                file (str): 文件名
                obj (str | dict[Any, Any] | list[Any]): JSON 对象
            """
            os.makedirs(f"{TOOLDELTA_PLUGIN_DATA_DIR}/{plugin_name}", exist_ok=True)
            with open(
                f"{TOOLDELTA_PLUGIN_DATA_DIR}/{plugin_name}/{file}.json", "w"
            ) as f:
                Utils.JsonIO.SafeJsonDump(obj, f, indent=indent)

    SimpleJsonDataReader = JsonIO

    class ChatbarLock:
        """
        聊天栏锁, 用于防止玩家同时开启多个聊天栏对话

        调用了该锁的所有代码, 在另一个进程使用该锁的时候, 尝试调用其他锁会导致进程直接退出, 直到此锁退出为止

        示例(以类式插件为例):
        ```python
        class MyPlugin(Plugin):
            ...
            def on_player_message(self, player: str, msg: str):
                with ChatbarLock(player):
                    # 如果玩家处在另一个on_player_message进程 (锁环境) 中
                    # 则在上面就会直接引发 SystemExit
                    ...
        ```
        示例(以注入式插件为例):
        ```
        @player_message()
        async def onPlayerChat(info: player_message_info):
            with ChatbarLock(info.playername):
                ...
        ```
        """

        def __init__(self, player: str, oth_cb: Callable[[str], None] = lambda _: None):
            self.player = player
            self.oth_cb = oth_cb

        def __enter__(self):
            if self.player in chatbar_lock_list:
                self.oth_cb(self.player)
                Print.print_war(f"玩家 {self.player} 的线程锁正在锁定状态")
                raise SystemExit
            if self.player not in chatbar_lock_list:
                chatbar_lock_list.append(self.player)

        def __exit__(self, e, e2, e3):
            chatbar_lock_list.remove(self.player)

    @staticmethod
    def get_threads_list() -> list["Utils.createThread"]:
        """返回使用 createThread 创建的全线程列表。"""
        return threads_list

    @staticmethod
    def simple_fmt(kw: dict[str, Any], sub: str) -> str:
        """
        快速将字符串内按照给出的 dict 的键值对替换掉内容.

        参数:
            kw: Dict[str, Any], 键值对应替换的内容
            *args: str, 需要被替换的字符串

        示例:
            >>> my_color = "red"; my_item = "apple"
            >>> kw = {"[颜色]": my_color, "[物品]": my_item}
            >>> Utils.SimpleFmt(kw, "I like [颜色] [物品].")
            I like red apple.
        """
        for k, v in kw.items():
            if k in sub:
                sub = sub.replace(k, str(v))
        return sub

    SimpleFmt = simple_fmt

    @staticmethod
    def simple_assert(cond: Any, exc: Any) -> None:
        """相当于 assert cond, 但是可以自定义引发的异常的类型"""
        if not cond:
            raise exc

    simpleAssert = simple_assert

    @staticmethod
    def thread_func(
        func_or_name: Callable | str, thread_level=ToolDeltaThread.PLUGIN
    ) -> Any:
        """
        在事件方法可能执行较久会造成堵塞时使用，方便快捷地创建一个新线程，例如:

        ```python
        @Utils.thread_func
        def on_inject(self):
            ...
        ```
        或者:
        ```python
        @Utils.thread_func("一个会卡一分钟的线程")
        def on_inject(self):
            ...
        ```
        """
        if isinstance(func_or_name, str):

            def _recv_func(func: Callable):
                def thread_fun(*args: tuple, **kwargs: Any) -> None:
                    Utils.createThread(
                        func,
                        usage=func_or_name,
                        thread_level=thread_level,
                        args=args,
                        **kwargs,
                    )

                return thread_fun

            return _recv_func

        def thread_fun(*args: tuple, **kwargs: Any) -> None:
            Utils.createThread(
                func_or_name,
                usage="简易线程方法：" + func_or_name.__name__,
                args=args,
                **kwargs,
            )

        return thread_fun

    @staticmethod
    def timer_event(
        t: int, name: str | None = None, thread_priority=ToolDeltaThread.PLUGIN
    ):
        """
        将修饰器下的方法作为一个定时任务, 每隔一段时间被执行一次。
        注意: 请不要在函数内放可能造成堵塞的内容
        注意: 当方法被 timer_event 修饰后, 需要调用一次该方法才能开始定时任务线程!

        Args:
            seconds (int): 周期秒数
            name (Optional[str], optional): 名字, 默认为自动生成的

        ```python
            @timer_event(60, "定时问好")
            def greeting():
                print("Hello!")
            greeting()
        ```
        """

        def receiver(func: Callable[[], None] | Callable[[Any], None]):
            def caller(*args, **kwargs):
                func_name = name or f"简易方法:{func.__name__}"
                timer_events_table.setdefault(t, [])
                timer_events_table[t].append(
                    (func_name, func, args, kwargs, thread_priority)
                )

            return caller

        return receiver

    @staticmethod
    def thread_gather(
        funcs_and_args: list[tuple[Callable[..., VT], tuple]],
    ) -> list[VT]:
        r"""
        使用回调线程作为并行器的伪异步执行器
        可以用于并发获取多个阻塞方法的返回
        ```
        >>> results = thread_gather([
            (requests.get, ("https://www.github.com",)),
            (time.sleep, (1,)),
            (sum, (1, 3, 5))
        ])
        >>> results
        [<Response 200>, None, 9]
        ```

        Args:
            funcs_and_args (list[tuple[Callable[..., VT], tuple]]): (方法, 参数) 的列表
        Returns

        Returns:
            list[VT]: 方法的返回 (按传入方法的顺序依次返回其结果)
        """
        res: list[Any] = [None] * len(funcs_and_args)
        oks = [False for _ in range(len(funcs_and_args))]
        for i, (func, args) in enumerate(funcs_and_args):

            def _closet(_i, _func):
                def _cbfunc(*args):
                    try:
                        assert isinstance(args, tuple), "传参必须是 tuple 类型"
                        res[_i] = _func(*args)
                    finally:
                        oks[_i] = True

                return _cbfunc

            fun, usage = _closet(i, func), f"并行方法 {func.__name__}"
            Utils.createThread(fun, args, usage=usage)
        while not all(oks):
            pass
        return res

    @staticmethod
    def try_int(arg: Any) -> int | None:
        """尝试将提供的参数化为 int 类型并返回，否则返回 None"""
        try:
            return int(arg)
        except Exception:
            return None

    @staticmethod
    def try_convert(
        arg: Any, factory: Callable[[Any], FACTORY_TYPE]
    ) -> FACTORY_TYPE | None:
        """
        尝试将提供的参数交给传入的 factory 处理并返回

        Args:
            arg (Any): 参数
            factory (Callable[[Any], factory_type]): 处理器方法

        Returns:
            factory_type | None: 处理结果, 遇到 ValueError 则返回 None

        >>> try_convert("4.5", float)
        4.5
        >>> print(try_convert("3", bool))
        None
        """
        try:
            return factory(arg)
        except Exception:
            return None

    @staticmethod
    def fuzzy_match(lst: list[str], sub: str) -> list[str]:
        """
        模糊匹配列表内的字符串，可以用在诸如模糊匹配玩家名的用途

        参数:
            lst: list, 字符串列表
            sub: str, 需要匹配的字符串
        返回:
            list, 匹配结果
        """
        res = []
        for i in lst:
            if sub in i:
                res.append(i)
        return res

    @staticmethod
    def split_list(lst: list[VT], length: int) -> list[list[VT]]:
        """
        将列表进行块分割

        Args:
            lst (list[VT]): 传入列表
            length (int): 分割的单个列表的长度

        Returns:
            list[list[VT]]: 传出的被分割的列表
        """
        return [lst[i : i + length] for i in range(0, len(lst), length)]

    @staticmethod
    def fill_list_index(lst: list[VT], default: list[VT]):
        """
        使用默认值填充列表。

        Args:
            lst (list[VT]): 待填充列表
            default (list[VT]): 默认的填充值 (补全待填充列表)
        """
        if len(lst) < len(default):
            lst.extend(default[len(lst) :])

    @staticmethod
    def remove_mc_color_code(string: str):
        return MC_COLOR_CODE_REG.sub("", string)

    @staticmethod
    def to_plain_name(name: str) -> str:
        """
        去除 网易版 Minecraft 的名字中的颜色代码
        可用于将 VIP 玩家名 转换为普通玩家名

        Args:
            name (str): 玩家名

        Returns:
            str: 去除颜色代码后的名字
        """
        if name.count("<") > 1:
            # <<VIP名><玩家名>> -> 玩家名
            cleaned_name = Utils.remove_mc_color_code(name)
            cached_str = ""
            words = []

            for char in cleaned_name:
                if char == "<":
                    cached_str = ""
                elif char == ">":
                    words.append(cached_str)
                else:
                    cached_str += char

            return words[-1]
        elif name.startswith("<") and name.endswith(">"):
            # <玩家名> -> 玩家名
            return name[1:-1]
        return name

    @staticmethod
    def to_player_selector(playername: str) -> str:
        """
        将玩家名转换为目标选择器.
        >>> to_player_selector("123坐端正")
        '@a[name="123坐端正"]'
        >>> to_player_selector('@a[name="123坐端正"]') # 已有选择器不会再套选择器
        '@a[name="123坐端正"]'

        Args:
            playername (str): 玩家名

        Returns:
            str: 含玩家名的目标选择器
        """
        if not playername.startswith("@"):
            return f'@a[name="{playername}"]'
        else:
            # 很可能这就已经是目标选择器了
            return playername

    @staticmethod
    def create_result_cb():
        """
        获取一对回调锁

        ```
        getter, setter = Utils.create_result_cb()

        cbs[special_id] = getter
        # 在这边等待回调...
        result = getter()

        # 与此同时, 在另一边...
        if special_id in cbs.keys():
            cbs[special_id](getting_data)

        ```
        """
        ret = [None]
        lock = threading.Lock()
        lock.acquire()

        def getter(timeout=60.0) -> Any:
            lock.acquire(timeout=timeout)
            return ret[0]

        def setter(s):
            ret[0] = s
            lock.release()

        return getter, setter


def safe_close():
    """安全关闭: 保存JSON配置文件和关闭所有定时任务"""
    if event_pool.get("timer_events"):
        event_pool["timer_events"].set()
    force_stop_common_threads()
    _tmpjson_save()
    timer_event_clear()
    jsonPathTmp.clear()
    jsonUnloadPathTmp.clear()


def if_token() -> None:
    """检查路径下是否有 fbtoken，没有就提示输入

    Raises:
        SystemExit: 未输入 fbtoken
    """
    if not os.path.isfile("fbtoken"):
        Print.print_inf(
            "请到对应的验证服务器官网下载 FBToken，并放在本目录中，或者在下面输入 fbtoken"
        )
        fbtoken = input(Print.fmt_info("请输入 fbtoken: ", "§b 输入 "))
        if fbtoken:
            with open("fbtoken", "w", encoding="utf-8") as f:
                f.write(fbtoken)
        else:
            Print.print_err("未输入 fbtoken, 无法继续")
            raise SystemExit


def fbtokenFix():
    """修复 fbtoken 里的换行符"""
    with open("fbtoken", encoding="utf-8") as file:
        token = file.read()
        if "\n" in token:
            Print.print_war("fbtoken 里有换行符，会造成 fb 登录失败，已自动修复")
            with open("fbtoken", "w", encoding="utf-8") as file2:
                file2.write(token.replace("\n", ""))


def _tmpjson_save(fp: str | None = None):
    "请不要在系统调用以外调用"
    if not fp:
        for k, (isChanged, dat) in jsonPathTmp.copy().items():
            if isChanged:
                Utils.SimpleJsonDataReader.SafeJsonDump(dat, k)
                jsonPathTmp[k][0] = False
        for k, v in jsonUnloadPathTmp.copy().items():
            if time.time() - v > 0:
                Utils.TMPJson.unloadPathJson(k)
                del jsonUnloadPathTmp[k]
    else:
        _, dat = jsonPathTmp[fp]
        Utils.SimpleJsonDataReader.SafeJsonDump(dat, fp)
        jsonPathTmp[fp][0] = False


def _shelve_save(fp: str | None = None):
    "请不要在系统调用以外调用"
    if not fp:
        for shelf in shelvePathTmp.copy().values():
            shelf.sync()
    else:
        shelvePathTmp[fp].close()


@Utils.timer_event(120, "缓存JSON数据定时保存", Utils.ToolDeltaThread.SYSTEM)
@Utils.thread_func("JSON 缓存文件定时保存", Utils.ToolDeltaThread.SYSTEM)
def tmpjson_save():
    "请不要在系统调用以外调用"
    _tmpjson_save()


@Utils.timer_event(120, "缓存JSON数据定时保存", Utils.ToolDeltaThread.SYSTEM)
@Utils.thread_func("JSON 缓存文件定时保存", Utils.ToolDeltaThread.SYSTEM)
def shelve_save():
    "请不要在系统调用以外调用"
    _shelve_save()


def timer_event_clear():
    "使用reload清理所有非系统线程"
    _timer_event_lock.acquire()
    for k, funcs_args in timer_events_table.copy().items():
        for func_args in funcs_args:
            (_, _, _, _, priority) = func_args
            if priority != Utils.ToolDeltaThread.SYSTEM:
                timer_events_table[k].remove(func_args)
        if timer_events_table[k] == []:
            del timer_events_table[k]
    _timer_event_lock.release()


def force_stop_common_threads():
    for i in threads_list:
        if i._thread_level != i.SYSTEM:
            Print.print_suc(f"正在终止线程 {i.usage}  ", end="\r")
            res = i.stop()
            if res:
                Print.print_suc(f"已终止线程 <{i.usage}>    ")
            else:
                Print.print_suc(f"无法终止线程 <{i.usage}>  ")


@Utils.thread_func("ToolDelta 定时任务", Utils.ToolDeltaThread.SYSTEM)
def timer_event_boostrap():
    "请不要在系统调用以外调用"
    timer = 0
    evt = event_pool["timer_events"] = threading.Event()
    evt.clear()
    Print.print_suc("已开始执行 ToolDelta定时任务 函数集.")
    while not evt.is_set():
        _timer_event_lock.acquire()
        for k, func_args in timer_events_table.copy().items():
            if timer % k == 0:
                for _, caller, args, kwargs, _ in func_args:
                    caller(*args, **kwargs)
        _timer_event_lock.release()
        evt.wait(1)
        timer += 1


jsonPathTmp: dict[str, list[bool | Any]] = {}
chatbar_lock_list = []
jsonUnloadPathTmp = {}
shelvePathTmp: dict[str, shelve.Shelf] = {}
