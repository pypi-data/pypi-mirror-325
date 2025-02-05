import pytest
from pymilvus import CollectionSchema, DataType, FieldSchema

from lego.db.vector_db.embed.openai_model import OpenAIEmbedModel
from lego.db.vector_db.milvus import MilvusDBConnector
from lego.db.vector_db.models import MilvusDBSettings
from lego.settings import MilvusConnection

TEST_COLLECTION = "test_collection"
MAXLEN = 128
DIM = 512


@pytest.fixture(scope="module")
def db():
    connection = MilvusConnection(uri="http://localhost:19530")
    settings = MilvusDBSettings(collection=TEST_COLLECTION)
    schema = CollectionSchema(
        fields=[
            FieldSchema(
                name="id",
                dtype=DataType.VARCHAR,
                is_primary=True,
                max_length=MAXLEN,
            ),
            FieldSchema(name="sql", dtype=DataType.VARCHAR, max_length=MAXLEN),
            FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=DIM),
        ]
    )
    return MilvusDBConnector(
        settings=settings,
        connection=connection,
        embed_model=OpenAIEmbedModel(embed_dim=DIM),
        schema=schema,
    )


@pytest.fixture(scope="module", autouse=True)
def setup(db):
    db.drop_collection()
    db.ensure_built()
    yield
    db.drop_partition()
    db.close()


@pytest.mark.first
def test_register_one(db):
    meta = {
        "id": "provide me the total sales",
        "sql": "SELECT SUM(sales) FROM sales",
    }
    item = meta.copy()
    item["vector"] = item["id"]
    assert db.count() == 0
    assert db.register_one(item)
    assert db.get(
        item["id"], output_fields=["id", "sql"], consistency_level="Session"
    ) == [meta]
    assert db.count() == 1
    assert db.register_one(item) is False
    assert db.count() == 1


@pytest.mark.second
def test_register_many(db):
    metas = [
        {
            "id": "provide me the total sales",
            "sql": "SELECT SUM(sales) FROM sales",
        },
        {
            "id": "show me the sales by region",
            "sql": "SELECT region, SUM(sales) FROM sales GROUP BY region",
        },
    ]
    items = [meta.copy() for meta in metas]
    ids = [item["id"] for item in metas]
    vecs = db.embed_model(ids)
    for item, vec in zip(items, vecs):
        item["vector"] = vec

    count = db.count()
    assert db.register_many(items) == 1
    assert (
        db.get(ids, output_fields=["id", "sql"], consistency_level="Session")
        == metas
    )
    assert db.count() == count + 1


@pytest.mark.third
def test_register_many_synthetic_sugar(db):
    metas = [
        {
            "id": "who is my priority customer",
            "sql": (
                "SELECT customer_id FROM sales GROUP BY customer_id"
                " ORDER BY SUM(sales) DESC LIMIT 1"
            ),
        },
        {
            "id": "who visited my website",
            "sql": "SELECT DISTINCT user_id FROM website_visits",
        },
        {
            "id": "update my sales target",
            "sql": "UPDATE sales SET target = target * 1.1",
        },
    ]
    items = [meta.copy() for meta in metas]
    ids = [item["id"] for item in metas]
    items[0]["vector"] = db.embed_model(items[0]["id"])
    items[1]["vector"] = items[1]["id"]

    count = db.count()
    with pytest.raises(KeyError, match="vector"):
        db.register_many(items)

    assert db.register_many(items, get_embeddings_from_primary_keys=True) == 3
    assert sorted(
        db.get(
            ids,
            output_fields=["id", "sql"],
            consistency_level="Session",
        ),
        key=lambda x: x["id"],
    ) == sorted(metas, key=lambda x: x["id"])
    assert db.count() == count + 3


@pytest.mark.fourth
def test_delete(db):
    assert db.delete("who visited my website") == 1
    assert not db.get("who visited my website", consistency_level="Strong")

    ## Not sure whether it is a bug or feature:
    ## but deleting once again will always return 1
    # assert db.delete("who visited my website") == 1

    db.delete()
    assert db.count() == 0
