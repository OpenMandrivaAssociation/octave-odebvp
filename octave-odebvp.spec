%define octpkg odebvp

Summary:	Function solving BVP ODE with Octave
Name:		octave-%{octpkg}
Version:	1.0.6
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 2.9.9

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
To approximate the solution of the boundary-value problem 
y''=p(x)*y' + q(x)*y + r(x), a<=x<=b, y(a)=alpha, y(b)=beta
by the linear finite-diffence method.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

