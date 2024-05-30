from django.contrib import admin

from wallet.models import Asset, Category, Market, Wallet


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price', 'quantity', 'total')
    search_fields = ('name', 'symbol')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('asset', 'category', 'market', 'description')
    search_fields = ('asset', 'category', 'market')
    list_filter = ('asset', 'category', 'market')
