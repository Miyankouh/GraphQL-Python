import graphene


class Query(graphene.ObjectType):
    name = graphene.String(username=graphene.String(default_value="user"))
    """
        is_admin == query-> {isAdmin}  
    """
    is_admin = graphene.Boolean()

    def resolve_name(self, info, username):
        return f"Hello {username}"

    def resolve_is_admin(self, info):
        return True


schema = graphene.Schema(query=Query, auto_camelcase=False)
result = schema.execute("""  
    {
        # name
        name(username: "majid")
    }
""")


print(result)
    