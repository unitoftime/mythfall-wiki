{% import "macros.tera" as macros %}

# All items
This is a list of ALL items present in Mythfall.

{{ macros::resourceTable(type=".*", hideModifiers=false) }}
