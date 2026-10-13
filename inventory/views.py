from django.shortcuts import render, redirect
from django.db.models import Q
from .models import ElectronicPart, ElectronicTool

def inventory_search_view(request):
    # --- Handle POST requests (Adding, Updating stock, or Deleting items) ---
    if request.method == 'POST':
        form_action = request.POST.get('form_action')

        # Scenario A: Adding a Brand New Item
        if form_action == 'add_item':
            item_type = request.POST.get('add_item_type')
            name = request.POST.get('name')
            qty = int(request.POST.get('quantity', 0))

            if name:
                if item_type == 'tool':
                    ElectronicTool.objects.create(
                        name=name,
                        brand=request.POST.get('brand', ''),
                        serial_number=request.POST.get('serial_number', ''),
                        quantity=qty
                    )
                elif item_type == 'part':
                    ElectronicPart.objects.create(
                        name=name,
                        part_number=request.POST.get('part_number', ''),
                        value=request.POST.get('value', ''),
                        package_type=request.POST.get('package_type', ''),
                        storage_location=request.POST.get('storage_location', ''),
                        quantity=qty
                    )

        # Scenario B: Inline Stock Modification
        elif form_action == 'update_stock':
            item_type = request.POST.get('item_type')
            item_id = request.POST.get('item_id')
            new_quantity = request.POST.get('quantity')

            try:
                qty = int(new_quantity)
                if qty >= 0:
                    if item_type == 'tool':
                        tool = ElectronicTool.objects.get(id=item_id)
                        tool.quantity = qty
                        tool.save()
                    elif item_type == 'part':
                        part = ElectronicPart.objects.get(id=item_id)
                        part.quantity = qty
                        part.save()
            except (ValueError, ElectronicTool.DoesNotExist, ElectronicPart.DoesNotExist):
                pass

        # Scenario C: Deleting an Item Completely
        elif form_action == 'delete_item':
            item_type = request.POST.get('item_type')
            item_id = request.POST.get('item_id')

            try:
                if item_type == 'tool':
                    ElectronicTool.objects.get(id=item_id).delete()
                elif item_type == 'part':
                    ElectronicPart.objects.get(id=item_id).delete()
            except (ElectronicTool.DoesNotExist, ElectronicPart.DoesNotExist):
                pass

        # Retain search query params across submissions
        query_string = request.GET.urlencode()
        url = request.path
        if query_string:
            url += f'?{query_string}'
        return redirect(url)

    # --- Handle GET requests (Displaying the tables and searching) ---
    query = request.GET.get('q')
    parts = ElectronicPart.objects.all()
    tools = ElectronicTool.objects.all()

    if query:
        parts = parts.filter(
            Q(name__icontains=query) |
            Q(part_number__icontains=query) |
            Q(value__icontains=query)
        )
        tools = tools.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(serial_number__icontains=query)
        )

    context = {
        'parts': parts,
        'tools': tools,
        'query': query
    }
    return render(request, 'inventory/part_list.html', context)
