from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from apps.medicines.models import Medicines
from apps.customers.models import Customers
from apps.sales.models import Sales


@login_required
def dashboard(request):

    medicine_count = Medicines.objects.count()

    customer_count = Customers.objects.count()

    low_stock_count = Medicines.objects.filter(
        stock_qty__lte=10
    ).count()

    today = timezone.localdate()

    today_sales = Sales.objects.filter(
        date__date=today
    )

    today_sales_total = today_sales.aggregate(
        total=Sum("total")
    )["total"] or 0

    recent_sales = Sales.objects.order_by("-date")[:5]

    low_stock_medicines = Medicines.objects.filter(
        stock_qty__lte=10
    )[:5]

    return render(
        request,
        "dashboard_section/dashboard.html",
        {
            "medicine_count": medicine_count,
            "customer_count": customer_count,
            "low_stock_count": low_stock_count,
            "today_sales_total": today_sales_total,
            "recent_sales": recent_sales,
            "low_stock_medicines": low_stock_medicines,
        }
    )
