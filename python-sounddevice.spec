Name:		python-sounddevice
Version:	0.5.6
Release:	2
Summary:	Play and record sound with Python
License:	MIT
Group:		Development/Python
URL:		https://python-sounddevice.readthedocs.io
Source0:	https://files.pythonhosted.org/packages/source/s/sounddevice/sounddevice-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(cffi)
Requires:	python%{pyver}dist(cffi)
Recommends:	pkgconfig(portaudio-2.0)

%description
PortAudio bindings for Python. Used by Aider for voice input.

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/sounddevice.py
%{py_sitedir}/_sounddevice.py
%{py_sitedir}/__pycache__/*sounddevice*
%{py_sitedir}/sounddevice-*.*-info
