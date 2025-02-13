import os

from src.bzapi.syncapi import AuthProvider, BzApi

atp = AuthProvider(username=os.environ["BZ_USER"], password=os.environ["BZ_PASSWORD"])
bz_api = BzApi(atp.auth_header)


def run_basic_chat_example():
    body = {
        "cursor": {"blockIndex": 0, "letterIndex": 20},
        "blocks": [{"isQuery": True, "text": "Why is the sky blue?"}],
    }
    text = ""
    for item in bz_api.streamed_chat_queries(body):
        delta = item["blocks"][1]["text"][len(text) :]
        text += delta
        print(delta, end="")


def run_chat_with_source_example():
    body = {
        "cursor": {"blockIndex": 0, "letterIndex": 20},
        "blocks": [{"isQuery": True, "text": "Why is the document about?"}],
        "sources": [{"fileId": "672ca9a87f4b91035eab1ebd", "type": "FILE"}],
    }
    text = ""
    for item in bz_api.streamed_chat_queries(body):
        delta = item["blocks"][1]["text"][len(text) :]
        text += delta
        print(delta, end="")


def list_files_example():
    print(bz_api.list_files())


def fetch_file_example():
    print(bz_api.fetch_file("66b9f31011c8f887c1aba4e7"))


if __name__ == "__main__":
    run_chat_with_source_example()
