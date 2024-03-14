class BookRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'book':
            return 'book'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'book':
            return 'book'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'book' or obj2._meta.app_label == 'book':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'book':
            return db == 'book'
        return None

class CartRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'cart':
            return 'cart'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'cart':
            return 'cart'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'cart' or obj2._meta.app_label == 'cart':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'cart':
            return db == 'cart'
        return None

class CatalogRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'catalog':
            return 'catalog'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'catalog':
            return 'catalog'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'catalog' or obj2._meta.app_label == 'catalog':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'catalog':
            return db == 'catalog'
        return None


class MobileRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'mobile':
            return 'mobile'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'mobile':
            return 'mobile'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'mobile' or obj2._meta.app_label == 'mobile':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'mobile':
            return db == 'mobile'
        return None

class ClotheRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'clothe':
            return 'clothe'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'clothe':
            return 'clothe'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'clothe' or obj2._meta.app_label == 'clothe':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'clothe':
            return db == 'clothe'
        return None

class PersonRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'person':
            return 'person'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'person':
            return 'person'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'person' or obj2._meta.app_label == 'person':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'person':
            return db == 'person'
        return None

class CategoryRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'category':
            return 'category'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'category':
            return 'category'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'category' or obj2._meta.app_label == 'category':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'category':
            return db == 'category'
        return None