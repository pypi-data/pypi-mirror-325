{% macro new_section(changes, title) -%}
{%- if changes %}
{{ title }}
{{ "-" * len(title) }}

{% for change in changes|sort(attribute="fulltitle") -%}
- {{ change.fulltitle }}{% if change.issue %} ({{ change.issue }}){% endif %}
  {%- if change.breaking_change %}
  *BREAKING CHANGE*: {{ change.breaking_change }}
  {%- endif %}
{% endfor -%}

{%- endif %}
{%- endmacro -%}

{{ changelog.version }} ({{ date.today().isoformat() }})
{{ "=" * len(changelog.version + " (" + date.today().isoformat() + ")") }}

{{- new_section(changelog.changes[ChangeType.feat], "🎉 New features") }}
{{- new_section(changelog.changes[ChangeType.perf], "🚀 Performance improvements") }}
{{- new_section(changelog.changes[ChangeType.fix], "👷 Bug fixes") }}
{{- new_section(changelog.changes[ChangeType.docs], "📝 Documentation") }}
{{- new_section(changelog.changes[ChangeType.ci], "🤖 Continuous integration") }}
{{- new_section(changelog.changes[ChangeType.unknown], "🤷 Various changes") }}
{{- new_section(changelog.changes[ChangeType.revert], "⏪️ Revert") }}
{{- new_section(changelog.changes[ChangeType.refactor], "🗜️ Refactoring") }}
{{- new_section(changelog.changes[ChangeType.test], "🧪 Tests") }}
{{- new_section(changelog.changes[ChangeType.chore], "🔧 Build process or tool changes") }}
{{- new_section(changelog.changes[ChangeType.style], "✨ Style") }}
