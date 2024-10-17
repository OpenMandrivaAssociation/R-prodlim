%global packname prodlim
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.7
Release:          1
Summary:          Product Limit Estimation for event history and survival analysis
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-core R-KernSmooth R-survival
BuildRequires:    R-devel texlive-collection-latex
BuildRequires:    R-KernSmooth R-survival

%description
Fast and user friendly nonparametric estimation in
censored survival (event history) analysis.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
