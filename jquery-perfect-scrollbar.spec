%define		plugin	perfect-scrollbar
Summary:	Minimalistic but perfect custom scrollbar plugin
Name:		jquery-%{plugin}
Version:	0.6.7
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/noraesae/perfect-scrollbar/releases/download/0.6.7/perfect-scrollbar.zip
# Source0-md5:	b785f9dce233243e9a169aa24ffdc938
URL:		https://noraesae.github.io/perfect-scrollbar/
BuildRequires:	unzip
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Minimalistic but perfect custom scrollbar plugin.

Perfect means:
- There's no css change on any original element
- Do not affect the original design layout
- The scrollbar css is fully customizable
- The scrollbar size and position can be updated

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

# js
cp -p js/min/perfect-scrollbar.jquery.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

cp -p js/perfect-scrollbar.jquery.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

# css
cp -p css/perfect-scrollbar.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.css

cp -p css/perfect-scrollbar.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.css
ln -s %{plugin}-%{version}.src.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
