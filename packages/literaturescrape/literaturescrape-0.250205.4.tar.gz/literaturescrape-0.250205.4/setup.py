import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="literaturescrape",
    version="0.250205.4",
    author="zzzzls",
    author_email="245129129@qq.com",
    description="Get literature information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zzzzls/",
    packages=setuptools.find_packages(),
    license='MIT',
    keywords=['literature', 'paper', 'doi', 'abstract'],
    install_requires=[
        "curl_cffi>=0.6.2",
        "loguru>=0.7.2"
    ]
)
