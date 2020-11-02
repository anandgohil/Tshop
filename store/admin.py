from django.contrib import admin
from store.models import Order,OrderItems,Payment, Tshirt, Cart, Occasion, IdealFor, NeckType, Sleeve, Brand, Colour, SizeVarient
from store.models.cart import Cart
from django.utils.html import format_html


# Register your models here.

class SizeVarientConfig(admin.TabularInline):
    model = SizeVarient

class OrderItemConfig(admin.TabularInline):
    model = OrderItems

class TshirtConfig(admin.ModelAdmin):
    inlines = [SizeVarientConfig]
    list_display = ['id','get_image','name','discount']
    list_editable = ['discount']
    sortable_by = ['name']
    list_filter = ['discount']
    list_display_links = ['name','id']
    search_fields = ['id','name']
    list_per_page = 5
    def get_image(self, obj):
        return format_html(f"""
        <a target="_blank" href = "{obj.image.url}"> <img src="{obj.image.url}" height="50px"> </a>
        """)

class CartConfig(admin.ModelAdmin):
    model = Cart
    # fields = ('sizevarient','quantity','user')

    list_display = ['quantity','size','tshirt', 'user','username']

    fieldsets = (
        ('Cart Info', {'fields': ('user','get_tshirt', 'get_sizevarient', 'quantity')}),
    )

    readonly_fields = ('quantity', 'user', 'get_sizevarient','get_tshirt')

    def get_sizevarient(self,obj):
        return obj.sizevarient.size

    get_sizevarient.short_description = 'Size'

    def get_tshirt(self,obj):
        tshirt = obj.sizevarient.tshirt
        tshirt_id = tshirt.id
        name = tshirt.name
        return format_html(f'<a href="/admin/store/tshirt/{tshirt_id}/change/" target="_blank">{name}</a>')
    get_tshirt.short_description = 'Tshirt'

    def size(self,obj):
        return obj.sizevarient.size

    def tshirt(self,obj):
        return obj.sizevarient.tshirt.name

    def username(self,obj):
        return obj.user.first_name

class OrderConfig(admin.ModelAdmin):
    list_display = ['user','shipping_addres', 'contact','date', 'order_status']
    fieldsets = (
        ('Order Info', {'fields': ('order_status','shipping_addres','contact','total','user')}),
        ("Payment Information" , {'fields' : ('paymant','payment_request_id','payment_id','payment_status') } ),

    )

    readonly_fields = ('user', 'contact', 'shipping_addres','total','payment_method','paymant','payment_request_id','payment_id','payment_status')

    inlines = [OrderItemConfig]

    def payment_request_id(self,obj):
        payment_request_id = obj.payment_set.all()[0].payment_request_id
        return payment_request_id

    def payment_status(self,obj):
        payment_status = obj.payment_set.all()[0].payment_status
        return payment_status

    def payment_id(self,obj):
        payment_id = obj.payment_set.all()[0].payment_id
        if payment_id is None or payment_id == '':
            return 'Payment Id is Not Available'
        else:
            return payment_id

    def paymant(self, obj):
        paymant_id = obj.payment_set.all()[0].id
        return format_html(f'<a href="/admin/store/payment/{paymant_id}/change/" target="_blank">Click for Payment Information</a>')


admin.site.register(Tshirt,TshirtConfig)
admin.site.register(Occasion)
admin.site.register(IdealFor)
admin.site.register(NeckType)
admin.site.register(Sleeve)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(SizeVarient)
admin.site.register(Cart,CartConfig)
admin.site.register(Order,OrderConfig)
admin.site.register(OrderItems)
admin.site.register(Payment)

