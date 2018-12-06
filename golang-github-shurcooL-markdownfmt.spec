# Run tests in check section
# Disable, isuue with latest blackfriday
%bcond_with check

%global goipath         github.com/shurcooL/markdownfmt
%global commit          5ba28a0bf0048ea9b00cecd23688dcf6cfb23fe5

%global common_description %{expand:
Markdown formatter.}

%gometa

Name:           %{goname}
Version:        1.1
Release:        0.3%{?dist}
Summary:        Markdown formatter
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(gopkg.in/russross/blackfriday.v1)
BuildRequires: golang(github.com/shurcooL/go/indentwriter)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup

# Replace blackfriday import path to avoid conflict with v2
sed -i 's|"github.com/russross/blackfriday|"gopkg.in/russross/blackfriday.v1|' $(find . -name '*.go')


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-0.3.20181026git5ba28a0
- Bump to commit 5ba28a0bf0048ea9b00cecd23688dcf6cfb23fe5
- Replace blackfriday import path

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.2.git10aae0a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-0.1.20180420git10aae0a
- First package for Fedora

