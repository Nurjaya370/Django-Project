from django.contrib import admin
from.models import Produk,Order

admin.site.site_header ="Aplikasi Penjualan Online"
admin.site.site_title="OlShop"
admin.site.index_title="Manage Online Shop"

class ProdukAdmin(admin.ModelAdmin):
    list_display=('Nama','harga','diskon','kategori','deskripsi','image')
    search_fields=('Nama',)

class OrderAdmin(admin.ModelAdmin):
    list_display=('items','nama','email','alamat','provinsi','kota','kecamatan','kelurahan','kodepos','total')
    search_fields=('nama',)
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Order, OrderAdmin)
