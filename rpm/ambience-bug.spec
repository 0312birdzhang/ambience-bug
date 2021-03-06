Name:       ambience-bug

Summary:    ambience test
Version:    0.0.1
Release:    1
Group:      System/GUI/Other
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake
Vendor: BirdZhang
Packager: BirdZhang

Requires:   ambienced

%description
This is a ambience made by birdzhang.

%package ts-devel
Summary:   Translation source for template ambience
License:   GPL
Group:     System/GUI/Other

%description ts-devel
Translation source for %name

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_datadir}/ambience/%{name}
%{_datadir}/ambience/%{name}/%{name}.ambience
%{_datadir}/ambience/%{name}/sounds.index
%{_datadir}/ambience/%{name}/images/*
%{_datadir}/ambience/%{name}/sounds/*
%{_datadir}/translations/%{name}_eng_en.qm

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/%{name}.ts

%post
systemctl-user restart ambienced.service

%changelog
* Fri Jun 26 2015 0312birdzhang
- first release
