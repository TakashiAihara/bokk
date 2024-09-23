import os
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from os import makedirs, path
from dataclasses import dataclass
from typing import Optional
import requests

icon_base_path = "/tmp/"
output_path = "images/"

def format_list_items(items):
    return "\n".join(f"- {item}" for item in items)

@dataclass
class IconData:
    url: str
    _download_path: Optional[str] = None

    @property
    def filename(self) -> str:
        return os.path.basename(self.url)

    @property
    def icon_path(self) -> str:
        if self._download_path is None:
            self._download_path = self._download_icon()
        return self._download_path

    def _download_icon(self) -> str:
        makedirs(icon_base_path, exist_ok=True)
        download_path = path.join(icon_base_path, self.filename)

        print(f"Downloading: {self.filename}")
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()

        with open(download_path, "wb") as f:
            f.write(response.content)

        print(f"Downloaded: {self.filename} to {download_path}")
        return download_path

class IconCollection:
    bookmarks = IconData("https://cdn-icons-png.flaticon.com/512/494/494568.png")
    reading_list = IconData("https://cdn2.iconfinder.com/data/icons/user-interface-ui-navigation-light/62/Book_Copy-512.png")
    chrome_extension = IconData("https://sato-icons.com/wp/wp-content/uploads/2020/09/%E3%83%91%E3%82%BA%E3%83%AB%E3%81%AE%E3%82%A2%E3%82%A4%E3%82%B3%E3%83%B3.png")
    chrome = IconData("https://cdn-icons-png.flaticon.com/512/220/220218.png")
    nestjs = IconData("https://static-00.iconduck.com/assets.00/nestjs-icon-1024x1020-34exj0g6.png")
    cli = IconData("https://cdn-icons-png.flaticon.com/512/1828/1828781.png")
    tidb = IconData("https://static.pingcap.co.jp/files/2023/07/09063705/TiDB-logo.png")
    hono = IconData("https://seeklogo.com/images/H/hono-logo-85A5D1206D-seeklogo.com.png")
    pulsar = IconData("https://datastax.gallerycdn.vsassets.io/extensions/datastax/develop-for-apache-pulsar/0.5.0/1690115444940/Microsoft.VisualStudio.Services.Icons.Default")
    valkey = IconData("https://valkey.io/img/favicon/android-chrome-144x144.png")
    nextjs = IconData("https://static-00.iconduck.com/assets.00/next-js-icon-2048x2048-5dqjgeku.png")
    react = IconData("https://cdn.icon-icons.com/icons2/3261/PNG/512/reactjs_logo_icon_206693.png")
    firefox = IconData("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Firefox_logo%2C_2019.svg/1200px-Firefox_logo%2C_2019.svg.png")

    @classmethod
    def __class_getitem__(cls, key: str) -> IconData:
        if hasattr(cls, key):
            return getattr(cls, key)
        raise KeyError(f"No icon named '{key}' found")

class NodeCollection:
    def bookmarks(self, name: str = "Bookmarks"):
      return Custom(name, icon_path=IconCollection.bookmarks.icon_path)

    def reading_list(self, name: str = "Reading List"):
      return Custom(name, icon_path=IconCollection.reading_list.icon_path)

    def chrome_extension(self, name: str = "Chrome Extension"):
      return Custom(name, icon_path=IconCollection.chrome_extension.icon_path)

    def chrome(self, name: str = "Chrome"):
        return Custom(name, icon_path=IconCollection.chrome.icon_path)

    def nestjs(self, name: str = "NestJS"):
        return Custom(name, icon_path=IconCollection.nestjs.icon_path)

    def cli(self, name: str = "CLI"):
        return Custom(name, icon_path=IconCollection.cli.icon_path)

    def tidb(self, name: str = "TiDB"):
        return Custom(name, icon_path=IconCollection.tidb.icon_path)

    def hono(self, name: str = "Hono"):
        return Custom(name, icon_path=IconCollection.hono.icon_path)

    def pulsar(self, name: str = "Pulsar"):
        return Custom(name, icon_path=IconCollection.pulsar.icon_path)

    def valkey(self, name: str = "Valkey"):
        return Custom(name, icon_path=IconCollection.valkey.icon_path)

    def nextjs(self, name: str = "NextJS"):
        return Custom(name, icon_path=IconCollection.nextjs.icon_path)

    def react(self, name: str = "React"):
        return Custom(name, icon_path=IconCollection.react.icon_path)

    def firefox(self, name: str = "Firefox"):
        return Custom(name, icon_path=IconCollection.firefox.icon_path)

class EdgeCollection:
    def trpc(self, name: str = ""):
        return Edge(label=name, color="Blue")

    def protobuf(self, name: str = ""):
        return Edge(label=name, color="Green")

    def type_safe(self, name: str = ""):
        return Edge(label=name, color="Red")

    def data(self, name: str = ""):
        return Edge(label=name, style="dotted")

class Legend:
    def __init__(self):
        class_name = self.__class__.__name__
        nodes = NodeCollection()
        edges = EdgeCollection()

        with Diagram(class_name, show=False, filename=output_path + class_name):
            nodes.hono("") \
                << edges.type_safe("Type Safe") \
                >> nodes.chrome_extension("")

            nodes.nestjs("") \
                << edges.trpc("tRPC") \
                >> nodes.hono("")

            nodes.nestjs("") \
                << edges.protobuf("protobuf") \
                >> nodes.pulsar("") \
                << edges.protobuf("protobuf") \
                >> nodes.nestjs("")

            nodes.chrome("") \
                >> edges.data("Data") \
                >> nodes.chrome_extension("")

class Sprint1:
    def __init__(self):
        class_name = self.__class__.__name__
        nodes = NodeCollection()
        edges = EdgeCollection()

        with Diagram(class_name + '"Chrome Sync"', show=False, filename=output_path + class_name):
            with Cluster("User"):
                extension_bff = nodes.hono("Extension BFF")

                with Cluster("Google Account"):
                    chrome = nodes.chrome()
                    bookmarks = nodes.bookmarks()
                    reading_list = nodes.reading_list()
                    extension = nodes.chrome_extension()

            with Cluster("Management"):
                cli_bff = nodes.hono("CLI BFF")
                cli = nodes.cli()

            with Cluster("System"):
                pulsar = nodes.pulsar()
                valkey = nodes.valkey()
                analytics_service = nodes.nestjs("Analytics Service")
                pages_service = nodes.nestjs("Pages Service")
                notification_service = nodes.nestjs("Notification Service")
                tidb = nodes.tidb("TiDB Serverless")

            chrome >> edges.data("Add Pages Data") >> extension
            bookmarks >> edges.data("Add Pages Data") >> extension
            reading_list >> edges.data("Add Pages Data") >> extension
            extension >> edges.type_safe("Pages Data") >> extension_bff

            valkey >> edges.protobuf("\n".join(["User Session", "Processed Data", "Status"])) << extension_bff
            extension_bff >> edges.protobuf() << pages_service

            cli >> edges.type_safe() << cli_bff
            cli_bff >> edges.protobuf() << pages_service
            cli_bff >> edges.protobuf("\n".join(["User Session", "Processed Data", "Status"])) >> valkey

            pages_service >> edges.protobuf("protobuf\nQueuing") >> pulsar
            pages_service >> tidb
            analytics_service >> tidb

            analytics_service >> edges.protobuf("Job Data") << pulsar
            analytics_service >> edges.protobuf("\n".join([
                "Processed Page",
                "Processing Status",
                "Data Cache"
            ])) >> valkey

            pulsar >> edges.protobuf("RealTime Notification") >> notification_service
            valkey >> edges.protobuf("OnTime Notification") >> notification_service
            notification_service >> edges.trpc("SSE Notification") >> extension

class Sprint2:
    def __init__(self):
        class_name = self.__class__.__name__
        nodes = NodeCollection()

        with Diagram(class_name + '"Bookmarks Integration"', direction="TB", show=False, filename=output_path + class_name):
            with Cluster("User"):
                extension_bff = nodes.hono("Extension BFF")
                user = nodes.react("User UI")
                user_bff = nodes.hono("Manager BFF")

                with Cluster("Google Account 1"):
                    chrome1 = nodes.chrome()
                    bookmarks1 = nodes.bookmarks()
                    reading_list1 = nodes.reading_list()
                    extension1 = nodes.chrome_extension()

                with Cluster("Google Account 2"):
                    chrome2 = nodes.chrome()
                    bookmarks2 = nodes.bookmarks()
                    reading_list2 = nodes.reading_list()
                    extension2 = nodes.chrome_extension()

                with Cluster("Firefox Account"):
                    firefox = nodes.firefox()
                    bookmarks_firefox = nodes.bookmarks()
                    extension_firefox = nodes.chrome_extension()

            with Cluster("Management"):
                cli = nodes.cli()
                cli_bff = nodes.hono("CLI BFF")
                manager = nodes.react("Manager UI")
                manager_bff = nodes.hono("Manager BFF")

            with Cluster("System"):
                pulsar = nodes.pulsar()
                valkey = nodes.valkey()
                analytics_service = nodes.nestjs("Analytics Service")
                pages_service = nodes.nestjs("Pages Service")
                tidb = nodes.tidb("TiDB Serverless")

            chrome1 >> Edge(label="Add") >> extension1
            extension1 >> Edge(label="Add/Sync") >> bookmarks1
            extension1 >> Edge(label="Add/Sync") >> reading_list1

            chrome2 >> Edge(label="Add") >> extension2
            extension2 >> Edge(label="Add/Sync") >> bookmarks2
            extension2 >> Edge(label="Add/Sync") >> reading_list2

            user >> Edge(label="Type Safe") >> user_bff

            firefox >> Edge(label="Add") >> extension_firefox
            extension_firefox >> Edge(label="Add/Sync") >> bookmarks_firefox

            manager >> Edge(label="Type Safe") >> manager_bff
            cli >> Edge(label="Type Safe") >> cli_bff
            cli_bff >> cli

            extension1 >> Edge(label="Type Safe") >> extension_bff
            extension2 >> Edge(label="Type Safe") >> extension_bff

            cli_bff >> Edge(label="tRPC") >> pages_service
            cli_bff >> Edge(label="User Session") >> valkey
            cli_bff >> Edge(label="Processed Data") >> valkey

            manager_bff >> Edge(label="tRPC") >> pages_service

            valkey >> Edge(label="Processing Status") >> cli_bff
            valkey >> Edge(label="User Session") >> extension_bff
            valkey >> Edge(label="Processed Page") >> extension_bff

            extension_bff >> Edge(label="Processing Status") >> valkey
            extension_bff >> Edge(label="tRPC") >> pages_service

            pages_service >> Edge(label="protobuf\nqueuing") >> pulsar
            pages_service >> tidb

            pulsar >> Edge(label="protobuf") >> analytics_service
            analytics_service >> Edge(label="protobuf") >> pulsar
            analytics_service >> Edge(label="Processed Page") >> valkey
            analytics_service >> Edge(label="Processing Status") >> valkey
            analytics_service >> Edge(label="Data Cache") >> valkey
            analytics_service >> tidb


Legend()
Sprint1()
Sprint2()