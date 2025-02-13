"""
Tests for the template tags
"""

# Django
from django.template import Context, Template
from django.test import TestCase, override_settings

# AA Discord Announcements
from aa_discord_announcements import __version__
from aa_discord_announcements.helper.static_files import calculate_integrity_hash


class TestVersionedStatic(TestCase):
    """
    Test aa_discord_announcements_static
    """

    @override_settings(DEBUG=False)
    def test_versioned_static(self):
        """
        Test versioned static template tag

        :return:
        """

        context = Context(dict_={"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load aa_discord_announcements %}"
                "{% aa_discord_announcements_static 'css/aa-discord-announcements.min.css' %}"
                "{% aa_discord_announcements_static 'javascript/aa-discord-announcements.min.js' %}"
            )
        )

        rendered_template = template_to_render.render(context=context)

        expected_static_css_src = f'/static/aa_discord_announcements/css/aa-discord-announcements.min.css?v={context["version"]}'
        expected_static_css_src_integrity = calculate_integrity_hash(
            "css/aa-discord-announcements.min.css"
        )
        expected_static_js_src = f'/static/aa_discord_announcements/javascript/aa-discord-announcements.min.js?v={context["version"]}'
        expected_static_js_src_integrity = calculate_integrity_hash(
            "javascript/aa-discord-announcements.min.js"
        )

        self.assertIn(member=expected_static_css_src, container=rendered_template)
        self.assertIn(
            member=expected_static_css_src_integrity, container=rendered_template
        )
        self.assertIn(member=expected_static_js_src, container=rendered_template)
        self.assertIn(
            member=expected_static_js_src_integrity, container=rendered_template
        )

    @override_settings(DEBUG=True)
    def test_versioned_static_with_debug_enabled(self) -> None:
        """
        Test versioned static template tag with DEBUG enabled

        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load aa_discord_announcements %}"
                "{% aa_discord_announcements_static 'css/aa-discord-announcements.min.css' %}"
            )
        )

        rendered_template = template_to_render.render(context=context)

        expected_static_css_src = f'/static/aa_discord_announcements/css/aa-discord-announcements.min.css?v={context["version"]}'

        self.assertIn(member=expected_static_css_src, container=rendered_template)
        self.assertNotIn(member="integrity=", container=rendered_template)
