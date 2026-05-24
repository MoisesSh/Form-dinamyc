from django.db import models

class Apps00Accountactivationcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=8)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    is_used = models.BooleanField()
    attempts = models.IntegerField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user = models.ForeignKey('Apps00Customuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_accountactivationcode'


class Apps00Accountactivationcodeexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=8)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    is_used = models.BooleanField()
    attempts = models.IntegerField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user = models.ForeignKey('Apps00Userexterno', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_accountactivationcodeexterno'


class Apps00Boosninesscategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.BooleanField()
    type = models.ForeignKey('Apps00Boosninesstype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_boosninesscategory'


class Apps00Boosninesstype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'apps_00_boosninesstype'


class Apps00Contactuserdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    mail_verified = models.IntegerField()
    email2 = models.CharField(max_length=254, blank=True, null=True)
    email2_verified = models.IntegerField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    user_id_telegram = models.CharField(max_length=20, blank=True, null=True)
    active_telegram = models.IntegerField()
    user = models.OneToOneField('Apps00Customuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_contactuserdata'


class Apps00Contactuserdataexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    mail_verified = models.IntegerField()
    email2 = models.CharField(max_length=254, blank=True, null=True)
    email2_verified = models.IntegerField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    user_id_telegram = models.CharField(max_length=20, blank=True, null=True)
    active_telegram = models.IntegerField()
    user = models.OneToOneField('Apps00Userexterno', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_contactuserdataexterno'


class Apps00Customuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(max_length=150, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    is_email_verified = models.BooleanField()
    email_verified_at = models.DateTimeField(blank=True, null=True)
    boosniness_data = models.ForeignKey('BoosninessData', models.DO_NOTHING, blank=True, null=True)
    rol = models.ForeignKey('Apps00Rol', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_customuser'


class Apps00CustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(Apps00Customuser, models.DO_NOTHING)
    group = models.ForeignKey('auth.Group', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_customuser_groups'
        unique_together = (('customuser', 'group'),)


class Apps00CustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(Apps00Customuser, models.DO_NOTHING)
    permission = models.ForeignKey('auth.Permission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class Apps00Emailverificationtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    is_used = models.BooleanField()
    user = models.ForeignKey(Apps00Customuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_emailverificationtoken'


class Apps00Emailverificationtokenexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    is_used = models.BooleanField()
    user = models.ForeignKey('Apps00Userexterno', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_emailverificationtokenexterno'


class Apps00Endpoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    identifier = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField()
    url_path = models.CharField(max_length=500)
    http_method = models.CharField(max_length=10)
    view_name = models.CharField(max_length=200)
    security_level = models.CharField(max_length=20)
    is_active = models.BooleanField()
    requires_https = models.BooleanField()
    rate_limit = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(Apps00Customuser, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('Apps00Endpointcategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_endpoint'
        unique_together = (('url_path', 'http_method'),)


class Apps00Endpointaccesslog(models.Model):
    id = models.BigAutoField(primary_key=True)
    access_granted = models.BooleanField()
    denial_reason = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    request_method = models.CharField(max_length=10)
    request_path = models.CharField(max_length=500)
    response_time_ms = models.IntegerField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    risk_score = models.IntegerField()
    is_suspicious = models.BooleanField()
    timestamp = models.DateTimeField()
    endpoint = models.ForeignKey(Apps00Endpoint, models.DO_NOTHING)
    user = models.ForeignKey(Apps00Customuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_endpointaccesslog'


class Apps00Endpointcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    order = models.IntegerField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'apps_00_endpointcategory'


class Apps00Endpointpermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField()
    can_read = models.BooleanField()
    can_write = models.BooleanField()
    can_delete = models.BooleanField()
    time_restrictions = models.JSONField()
    ip_restrictions = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(Apps00Customuser, models.DO_NOTHING, blank=True, null=True)
    endpoint = models.ForeignKey(Apps00Endpoint, models.DO_NOTHING)
    group = models.ForeignKey('auth.Group', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('Apps00Rol', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_endpointpermission'
        unique_together = (('endpoint', 'group'), ('endpoint', 'role'),)


class Apps00Notificacionsistema(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField()
    tipo = models.CharField(max_length=20)
    importancia = models.CharField(max_length=10)
    emoji = models.CharField(max_length=10, blank=True, null=True)
    leida = models.BooleanField()
    fecha_lectura = models.DateTimeField(blank=True, null=True)
    metadatos = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    enviada_telegram = models.BooleanField()
    enviada_websocket = models.BooleanField()
    fecha_envio_telegram = models.DateTimeField(blank=True, null=True)
    fecha_envio_websocket = models.DateTimeField(blank=True, null=True)
    usuario_destinatario = models.ForeignKey(Apps00Customuser, models.DO_NOTHING)
    usuario_responsable = models.ForeignKey(Apps00Customuser, models.DO_NOTHING, related_name='apps00notificacionsistema_usuario_responsable_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_notificacionsistema'


class Apps00Pageaccesslog(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    url_accessed = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    method = models.CharField(max_length=10)
    browser = models.CharField(max_length=200, blank=True, null=True)
    device_type = models.CharField(max_length=50, blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    response_time = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(Apps00Customuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_pageaccesslog'


class Apps00Passwordrecoverycode(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=8)
    is_used = models.BooleanField()
    attempts = models.IntegerField()
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey('Apps00Userexterno', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_passwordrecoverycode'


class Apps00Phoneactivationcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=6)
    created_at = models.DateTimeField()
    is_used = models.BooleanField()
    expires_at = models.DateTimeField()
    contact_user_data = models.ForeignKey(Apps00Contactuserdata, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_phoneactivationcode'


class Apps00Phoneactivationcodeexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=6)
    created_at = models.DateTimeField()
    is_used = models.BooleanField()
    expires_at = models.DateTimeField()
    contact_user_data = models.ForeignKey(Apps00Contactuserdataexterno, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_phoneactivationcodeexterno'


class Apps00Rol(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'apps_00_rol'


class Apps00Securityauditlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    browser = models.CharField(max_length=200, blank=True, null=True)
    operating_system = models.CharField(max_length=200, blank=True, null=True)
    device_type = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50)
    url_accessed = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    success = models.BooleanField()
    user = models.ForeignKey(Apps00Customuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_securityauditlog'


class Apps00Securityauditlogexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    browser = models.CharField(max_length=200, blank=True, null=True)
    operating_system = models.CharField(max_length=200, blank=True, null=True)
    device_type = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50)
    url_accessed = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    success = models.BooleanField()
    user = models.ForeignKey('Apps00Userexterno', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_securityauditlogexterno'


class Apps00Userexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(max_length=150, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    is_email_verified = models.BooleanField()
    email_verified_at = models.DateTimeField(blank=True, null=True)
    boosniness_data = models.ForeignKey('BoosninessData', models.DO_NOTHING, blank=True, null=True)
    rol = models.ForeignKey(Apps00Rol, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_userexterno'


class Apps00UserexternoGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    userexterno = models.ForeignKey(Apps00Userexterno, models.DO_NOTHING)
    group = models.ForeignKey('auth.Group', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_userexterno_groups'
        unique_together = (('userexterno', 'group'),)


class Apps00UserexternoUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    userexterno = models.ForeignKey(Apps00Userexterno, models.DO_NOTHING)
    permission = models.ForeignKey('auth.Permission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_userexterno_user_permissions'
        unique_together = (('userexterno', 'permission'),)


class Apps00Usersession(models.Model):
    id = models.BigAutoField(primary_key=True)
    refresh_token = models.CharField(max_length=500)
    access_token = models.CharField(max_length=500)
    ip_address = models.GenericIPAddressField()
    device_info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    last_activity = models.DateTimeField()
    is_active = models.BooleanField()
    user = models.ForeignKey(Apps00Customuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_usersession'


class Apps00Usersessionexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    device_info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    last_activity = models.DateTimeField()
    is_active = models.BooleanField()
    user = models.ForeignKey(Apps00Userexterno, models.DO_NOTHING)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    session_duration_minutes = models.IntegerField()
    session_expires_at = models.DateTimeField(blank=True, null=True)
    session_start = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_00_usersessionexterno'


class Apps00Usertrustedip(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    last_used = models.DateTimeField()
    first_used = models.DateTimeField()
    is_trusted = models.BooleanField()
    login_count = models.IntegerField()
    user = models.ForeignKey(Apps00Customuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_usertrustedip'
        unique_together = (('user', 'ip_address'),)


class Apps00Usertrustedipexterno(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    last_used = models.DateTimeField()
    first_used = models.DateTimeField()
    is_trusted = models.BooleanField()
    login_count = models.IntegerField()
    user = models.ForeignKey(Apps00Userexterno, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_00_usertrustedipexterno'
        unique_together = (('user', 'ip_address'),)


class Apps07Qrcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    qr_id = models.CharField(unique=True, max_length=100)
    qr_image_base64 = models.TextField()
    redirect_url = models.CharField(max_length=200)
    secret_key = models.CharField(unique=True, max_length=100)
    purpose = models.CharField(max_length=200)
    size = models.IntegerField()
    border = models.IntegerField()
    error_correction = models.CharField(max_length=1)
    fill_color = models.CharField(max_length=20)
    back_color = models.CharField(max_length=20)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    metadata = models.JSONField()
    user = models.ForeignKey(Apps00Customuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_07_qrcode'


class BoosninessData(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rif = models.CharField(unique=True, max_length=255)
    logo = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Apps00Boosninesscategory, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey(Apps00Boosninesstype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boosniness_data'


class Estatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    id_tipo_estatus = models.ForeignKey('TipoEstatus', models.DO_NOTHING, db_column='id_tipo_estatus', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estatus'


class TipoEstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_estatus'
