from django.core import paginator
from django.shortcuts import render
from .models import Produk, Order
from django.core.paginator import Paginator

def index(request):
    produk_objects = Produk.objects.all()
    #membuat fungsi search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        produk_objects = produk_objects.filter(Nama__icontains=item_name)
    
    # membuat fungsi paginasi
    paginator = Paginator(produk_objects,8)
    page = request.GET.get('page')
    produk_objects = paginator.get_page(page)
        
    return render(request,'olshop/index.html',{'produk_objects':produk_objects})
def detail(request,id):
    produk_objects = Produk.objects.get(id=id)
    return render(request,'olshop/detail.html',{'produk_objects':produk_objects})

def checkout(request):
    if request.method == "POST":
        items= request.POST.get('items','')
        nama = request.POST.get('nama',"")
        email = request.POST.get('email',"")
        alamat = request.POST.get('alamat',"")
        provinsi = request.POST.get('provinsi',"")
        kota = request.POST.get('kota',"")
        kecamatan = request.POST.get('kecamatan',"")
        kelurahan = request.POST.get('kelurahan',"")
        kodepos = request.POST.get('kodepos',"")
        total = request.POST.get('total',"")
        order = Order(items=items, nama=nama, email=email, alamat=alamat, provinsi=provinsi, kota=kota, 
                      kecamatan=kecamatan, kelurahan=kelurahan, kodepos=kodepos, total=total)
        order.save()
    return render(request,'olshop/checkout.html')
    

    
    

    
