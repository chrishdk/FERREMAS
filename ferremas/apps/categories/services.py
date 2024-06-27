from .models import Category

def created_category (category):
    if Category.objects.filter(category=category).exists():
        return False, "La categoría ya existe"
    else:
        Category.objects.create(category=category)
        return True, "Categoría creada correctamente"
