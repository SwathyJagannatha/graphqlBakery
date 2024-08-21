import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Bakery as BakeryModel, db

class Bakery(SQLAlchemyObjectType):
    class Meta:
        model = BakeryModel

class Query(graphene.ObjectType):
    bakeries = graphene.List(Bakery)
    bakery_search = graphene.List(Bakery, name = graphene.String(),price = graphene.Int(),quantity = graphene.Int(),category = graphene.String())

    def resolve_bakeries(self, info):
        return db.session.execute(db.select(BakeryModel)).scalars()
    
    def resolve_bakery_search(self,info,name=None,price=None,quantity=None,category=None):
        query = db.select(BakeryModel)
        if name:
            query = query.where(BakeryModel.name.ilike(f'%{name}%'))
        if price:
            query = query.where(BakeryModel.price.ilike(f'%{price}%'))
        if quantity:
            query = query.where(BakeryModel.quantity.ilike(f'%{quantity}%'))
        if category:
            query = query.where(BakeryModel.category.ilike(f'%{category}%'))
        results = db.session.execute(query).scalars().all()
        return results 

class AddBakery(graphene.Mutation): #Creating our addMovie Mutation
    class Arguments: #the arguments required to add a movie
        name = graphene.String(required=True)
        price = graphene.Int(required=True)
        quantity = graphene.Int(required=True)
        category = graphene.String(required=True)
    
    bakery = graphene.Field(Bakery)

    def mutate(self, info, name, price, quantity,category): #This is the function that runs when the mutation is called
        bakery = BakeryModel(name=name, price=price, quantity=quantity,category=category) #Creating an instance of MovieModel
        db.session.add(bakery)
        db.session.commit() #add movie to our database

        db.session.refresh(bakery) #just incase the movie becomes detached from our session
        return AddBakery(bakery=bakery)

class DeleteBakery(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    bakery = graphene.Field(Bakery)

    def mutate(self,info,id):
        bakery = db.session.get(BakeryModel,id)

        if not bakery:
            return None
        
        db.session.delete(bakery)
        db.session.commit()

        return DeleteBakery(bakery = bakery)

class UpdateBakery(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        price = graphene.Int(required=False)
        quantity = graphene.Int(required=False)
        category = graphene.String(required=False)

    bakery = graphene.Field(Bakery)

    def mutate(self,info,id,name=None, price=None, quantity=None,category=None):
        bakery = db.session.get(BakeryModel,id)
        if not bakery:
            return None
        if name:
            bakery.name = name
        if price:
            bakery.price = price
        if quantity:
            bakery.quantity = quantity
        if category:
            bakery.category = category

        db.session.add(bakery)
        db.session.commit()
        db.session.refresh(bakery)
        return UpdateBakery(bakery = bakery)
    
class Mutation(graphene.ObjectType):
    create_bakery = AddBakery.Field()
    update_bakery = UpdateBakery.Field()
    delete_bakery = DeleteBakery.Field()