
import base64

str = "eyJib2R5IjogIlcxc2laRGt4T1dZd01tVmhNakUwTkRWa1lqbG1OVGhoWVRWaE9HUTNaR1k0WkRZaVhTd2dlMzBzSUhzaVkyRnNiR0poWTJ0eklqb2diblZzYkN3Z0ltVnljbUpoWTJ0eklqb2diblZzYkN3Z0ltTm9ZV2x1SWpvZ2JuVnNiQ3dnSW1Ob2IzSmtJam9nYm5Wc2JIMWQiLCAiY29udGVudC1lbmNvZGluZyI6ICJ1dGYtOCIsICJjb250ZW50LXR5cGUiOiAiYXBwbGljYXRpb24vanNvbiIsICJoZWFkZXJzIjogeyJsYW5nIjogInB5IiwgInRhc2siOiAiYXBwX3B1c2hfbmV3X21lZXRpbmciLCAiaWQiOiAiODYwNWE2OGUtYjYwYS00YzQzLWFhMzktZWY4ODdhYzQ0ZTA0IiwgImV0YSI6IG51bGwsICJleHBpcmVzIjogbnVsbCwgImdyb3VwIjogbnVsbCwgInJldHJpZXMiOiAwLCAidGltZWxpbWl0IjogW251bGwsIG51bGxdLCAicm9vdF9pZCI6ICI4NjA1YTY4ZS1iNjBhLTRjNDMtYWEzOS1lZjg4N2FjNDRlMDQiLCAicGFyZW50X2lkIjogbnVsbCwgImFyZ3NyZXByIjogIignZDkxOWYwMmVhMjE0NDVkYjlmNThhYTVhOGQ3ZGY4ZDYnLCkiLCAia3dhcmdzcmVwciI6ICJ7fSIsICJvcmlnaW4iOiAiZ2VuNzBAZTYwYmMzMTcyZjA0In0sICJwcm9wZXJ0aWVzIjogeyJjb3JyZWxhdGlvbl9pZCI6ICI4NjA1YTY4ZS1iNjBhLTRjNDMtYWEzOS1lZjg4N2FjNDRlMDQiLCAicmVwbHlfdG8iOiAiOGUwZWI1MGMtYzY4NC0zZjliLWEwYjctNmEwN2I3OWQyNGNmIiwgImRlbGl2ZXJ5X21vZGUiOiAyLCAiZGVsaXZlcnlfaW5mbyI6IHsiZXhjaGFuZ2UiOiAiIiwgInJvdXRpbmdfa2V5IjogIjg4LXB1c2gtZGV2In0sICJwcmlvcml0eSI6IDAsICJib2R5X2VuY29kaW5nIjogImJhc2U2NCIsICJkZWxpdmVyeV90YWciOiAiZWZlNDExMjMtOWNjMS00ZGFhLWIyZTItZTE2NGU0NTcyNTVmIn19"

output = ""

print(base64.b64decode(str))
print(base64.b64decode(str.decode()))
