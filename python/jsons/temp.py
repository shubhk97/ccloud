import barentsz


serializers = barentsz.discover_functions('./serializers', include_privates=False, in_private_modules=True)

print(1)