from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Home view to display products and the form to add a new product
def home(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # ✅ Added request.FILES
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    
    prod = Product.objects.all()
    return render(request, "Clothes/home.html", {'prod': prod, 'form': form})

# Update view to update a product
def update_data(request, id):
    pi = Product.objects.get(pk=id)
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES, instance=pi)  # ✅ Include request.FILES for image updates
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = ProductForm(instance=pi)
    return render(request, "Clothes/updates.html", {'form': fm})

# Delete view to delete a product
def delete_data(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('home')
