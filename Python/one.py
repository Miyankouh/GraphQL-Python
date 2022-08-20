import graphene
import json


class Query(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, info):
        return 'Hello user'


schema = graphene.Schema(query=Query)
result = schema.execute("""  
    query {
        name
    }
""")


# json
j = json.dumps(dict(result.data), indent=2)


if __name__ == '__main__':
    print(result)
    print(result.data)
    print(result.data.items())
    print(result.data.values())
    print(result.data['name'])
    print(j)
