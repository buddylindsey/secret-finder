# SecretFinder 🕵️

Have you ever had secerts for you apps in multiple places? Some are environment variables. Others are in a 3rd party providers like AWS SSM, AWS Secrets Manager, Hashicorp Vault, or any other number of places.  

Pulling from these locations can be frustrating if you have 2 or 3 in one app for various reasons.

Secret finder provides you a way to have a single unified api to pull from any number of locations.

## Install

```
pip install secretfinder
```

## Examples

### Environment Variables
You can pull from environment variables easily enough. This is almost useless since you can use `os.getenv`, but it has it purpose.

```python
from secretfinder import SecretsEnv, providers

env = SecretsEnv(providers=providers.EnvironmentVariable)

env.get('SOME_VAR', default='hello world')
```

### AWS SSM

If you are using AWS SSM to store your keys or other information, a lot of reasons to use it. You can see it works just the same as environment variables.

```python
from secretfinder import SecretsEnv, providers

env = SecretsEnv(providers=providers.AWSSSM)

env.get('prod.moneymaker.db', default='hello world')
```

### AWS Secrets Manager

If you are using AWS Secrets Manager to store your secrets because maybe you want to auto-rotate passwords then you can easily use it.

```python
from secretfinder import SecretsEnv, providers

env = SecretsEnv(providers=providers.AWSSecretsManager)

env.get('prod.moneymaker.db', default='hello world')
```

This still has limited support, but it works for other text secret types. It is a todo to expand it.

### AWS SSM and AWS Secrets Manager

You might be storing information in both SSM and Secrets Manager. Either you are in the middle of migrating from one to the other, or you have specific information in each for separation concerns.

No problem you still have a similar API you can use.

```python
from secretfinder import SecretsEnv, providers

env = SecretsEnv(providers=[providers.AWSSecretsManager, providers.AWSSSM])

env.get('prod.moneymaker.db', default='hello world')
```

This will just fall through all providers until it finds a match, or it returns a default.

There is logging in place to throw out warning when it can't find a value for a provider.

### HashiCorp Vault

Coming Soon

### Raise Exceptions

In the default use case it just falls through returning back a default or None. However, you might want it to raise an exception so that it stops execution if it fails.

In that case you can use the `raise_exception` keyword argument to raise.

```python
from secretfinder import SecretsEnv, providers

env = SecretsEnv(providers=providers.AWSSecretsManager, raise_exception=True)

env.get('prod.moneymaker.db', default='hello world')
```

## Contributing

If you would like to help expand the work on this please feel free submit a PR. Adding more providers would be greate, or filling out code for exising providers.


### Testing aws locally
If you are using aws and wanting to test locally with different profile. Here is what I had to use to get it to work right.

```
$ AWS_PROFILE=somprofile AWS_DEFAULT_REGION=us-east-2 ipython
```

## Release

```
pip install twine wheel setuptools
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
```
