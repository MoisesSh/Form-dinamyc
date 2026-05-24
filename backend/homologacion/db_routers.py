class EsquemaUserRouter:
    """
    Un enrutador para controlar todas las operaciones de base de datos
    de la app 'user' y la blacklist de tokens hacia el nuevo esquema.
    """
    # Define aquí las apps que se mudarán al nuevo esquema
    APPS_EN_NUEVO_ESQUEMA = {'user', 'token_blacklist'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.APPS_EN_NUEVO_ESQUEMA:
            return 'esquema_user'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.APPS_EN_NUEVO_ESQUEMA:
            return 'esquema_user'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Permite relaciones si ambas apps están en el mismo esquema"""
        if (
            obj1._meta.app_label in self.APPS_EN_NUEVO_ESQUEMA or
            obj2._meta.app_label in self.APPS_EN_NUEVO_ESQUEMA
        ):
            return obj1._meta.app_label in self.APPS_EN_NUEVO_ESQUEMA and obj2._meta.app_label in self.APPS_EN_NUEVO_ESQUEMA
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.APPS_EN_NUEVO_ESQUEMA:
            return db == 'esquema_user'
        return db == 'default'