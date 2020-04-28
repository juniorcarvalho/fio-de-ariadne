from django.contrib import admin
from django.utils.safestring import mark_safe

from web.core.models import Kid, KidImage


class KidImageInline(admin.TabularInline):
    model = KidImage
    fields = ["image", "image_render"]
    readonly_fields = ["image_render"]

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(KidImageInline, self).get_formset(request, obj, **kwargs)
        form = formset.form
        form.base_fields["image"].widget.attrs["accept"] = ".jpg,.jpeg,.png,*.gif"
        return formset

    def image_render(self, obj):
        return obj.image_render

    image_render.short_description = "Foto"

    class Media:
        pass


class KidModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "original",
        "dob",
        "missing_since",
        "eyes_display",
        "hair_display",
        "skin_display",
        "last_seen_at_city",
        "last_seen_at_state",
        "age_at_occurrence",
        "first_image",
    )
    list_filter = (
        "eyes",
        "hair",
        "skin",
        "last_seen_at_city",
        "last_seen_at_state",
        "age_at_occurrence",
    )

    inlines = [KidImageInline]

    def original(self, obj):
        label = "Ver link original"
        image = f'<img src="/static/admin/img/icon-viewlink.svg" alt="{label}">'
        return mark_safe(f'<a href="{obj.url}">{image}</a>')

    def eyes_display(self, obj):
        return obj.get_eyes_display()

    def hair_display(self, obj):
        return obj.get_hair_display()

    def skin_display(self, obj):
        return obj.get_skin_display()

    def first_image(self, obj):
        kid_image = KidImage.objects.filter(kid=obj).first()
        return kid_image.image_render if kid_image else None

    eyes_display.short_description = "Cor dos olhos"
    hair_display.short_description = "Cor dos cabelos"
    skin_display.short_description = "Cor da pele"
    first_image.short_description = "Foto"


admin.site.register(Kid, KidModelAdmin)
admin.site.site_header = "Ariadne"
admin.site.site_title = "Intranet"
admin.site.index_title = "Fio de Ariadne"
