"""mongodb异步库"""
import asyncio
import motor.motor_asyncio
import pytest

from motor.core import AgnosticCollection

from pymongo.results import InsertOneResult, InsertManyResult, UpdateResult, DeleteResult
from pymongo import ReturnDocument, ASCENDING, DESCENDING


@pytest.fixture
def coll():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test"]
    coll = db["test"]

    return coll


def test_link():
    """建立引用，不用IO"""
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

    db = client["test"]

    coll = db["test"]

    assert isinstance(coll, AgnosticCollection)


def test_insert(coll: AgnosticCollection):
    async def func():
        doc = {"key": "value"}
        result = await coll.insert_one(doc)

        assert isinstance(result, InsertOneResult)
        assert hasattr(result, "inserted_id")

    asyncio.run(func())


def test_insert_many(coll: AgnosticCollection):
    async def func():
        docs = [{"i": i} for i in range(10)]
        result = await coll.insert_many(docs)

        assert isinstance(result, InsertManyResult)
        assert hasattr(result, "inserted_ids")

    asyncio.run(func())


def test_find_one(coll: AgnosticCollection):
    """if exist, return doc"""
    async def func():
        filter = {"i": 1}
        result = await coll.find_one(filter)

        assert isinstance(result, dict)

    asyncio.run(func())


def test_find_one_noexist(coll: AgnosticCollection):
    """if noexist, return None"""
    async def func():
        filter = {"i": 10}
        result = await coll.find_one(filter)

        assert result is None

    asyncio.run(func())


def test_find(coll: AgnosticCollection):
    """coll.find() -> Cursor"""
    async def func():
        filter = {"i": {"$lt": 5}}
        cur = coll.find(filter).sort("i")

        async for doc in cur:
            print(doc)

    asyncio.run(func())


def test_find_2(coll: AgnosticCollection):
    """sort, skip, limit

    multi fields：coll.find().sort([('field1', pymongo.ASCENDING), ('field2', pymongo.DESCENDING)])
    """
    async def func():
        filter = {"i": {"$gt": 0}}
        cur = coll.find(filter).sort("i", DESCENDING).skip(1).limit(2)

        async for doc in cur:
            print(doc)

    asyncio.run(func())


def test_count(coll: AgnosticCollection):
    async def func():
        filter = {}
        count = await coll.count_documents(filter)
        print(count)

    asyncio.run(func())


def test_update_one(coll: AgnosticCollection):
    """update_one不会返回文档，而是返回UpdateResult"""
    async def func():
        filter = {"i": 0}
        update = {"$set": {"i": 10}}
        result = await coll.update_one(filter, update)

        assert isinstance(result, UpdateResult)
        assert hasattr(result, "matched_count")
        assert hasattr(result, "modified_count")

    asyncio.run(func())


def test_find_one_and_update(coll: AgnosticCollection):
    """未命中，返回None；命中，则默认返回old_doc，修改return_document(keyword arguments)可返回new_doc"""
    async def func():
        filter = {"i": 10}
        update = {"$set": {"i": 0}}
        result = await coll.find_one_and_update(filter, update, return_document=ReturnDocument.AFTER)

        assert isinstance(result, dict)

    asyncio.run(func())


def test_delete(coll: AgnosticCollection):
    """不返回文档，返回DeleteResult"""
    async def func():
        filter = {"key": "value"}
        result = await coll.delete_one(filter)

        assert isinstance(result, DeleteResult)
        assert hasattr(result, "deleted_count")

    asyncio.run(func())


def test_find_one_and_delete(coll: AgnosticCollection):
    """返回被删除文档"""
    async def func():
        filter = {"key": "value"}
        result = await coll.find_one_and_delete(filter)

        assert isinstance(result, dict)

    asyncio.run(func())


def test_projection(coll: AgnosticCollection):
    async def func():
        await coll.insert_one({"x": 1, "y": 1, "z": 1})

        result = await coll.find_one({}, projection={"_id": 0})
        print(result)

        assert isinstance(result, dict)

    asyncio.run(func())


def test_sort_str(coll: AgnosticCollection):
    """string comparison"""
    from datetime import datetime
    import random

    async def func():
        for _ in range(10):
            await asyncio.sleep(random.random())
            await coll.insert_one({"string_comparison": 1, "time": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")})

        cur = coll.find({"string_comparison": 1}, projection={"_id": 0, "time": 1}, sort=[("time", 1)])

        async for doc in cur:
            print(doc)

    asyncio.run(func())


def test_array_length(coll: AgnosticCollection):
    """AttributeError: 'AsyncIOMotorCursor' object has no attribute 'forEach'"""
    async def func():
        import bson
        for _ in range(10):
            await coll.insert_one({"test_array_length": 1, "array": [1]})
            await coll.insert_one({"test_array_length": 1, "array": [1, 2]})
            await coll.insert_one({"test_array_length": 1, "array": [1, 2, 3]})

        await coll.find({"test_array_length": 1}).forEach(bson.Code("""
            function(doc){
                coll.update({"_id": doc._id}, {"size": doc.array.length})
            }
        """))

        cur = coll.find({"test_array_length": 1}, projection={"_id": 0, "size": 1}, sort=[("size", 1)])
        async for doc in cur:
            print(doc)

    asyncio.run(func())


if __name__ == "__main__":
    pytest.main(["-s", f"{__file__}::{test_array_length.__name__}"])
