# revision 30450
# category Package
# catalog-ctan /macros/latex/contrib/embrac
# catalog-date 2013-05-13 20:07:16 +0200
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-embrac
Version:	0.4
Release:	4
Summary:	Upright brackets in emphasised text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/embrac
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embrac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embrac.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package redefines the commands \emph and \textit so that
parentheses and square brackets are typeset in an upright font
in their arguments. The package requires expl3 from the
l3kernel bundle, and xparse and l3keys2e from the l3packages
bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/embrac/embrac.sty
%doc %{_texmfdistdir}/doc/latex/embrac/README
%doc %{_texmfdistdir}/doc/latex/embrac/embrac_en.pdf
%doc %{_texmfdistdir}/doc/latex/embrac/embrac_en.tex
%doc %{_texmfdistdir}/doc/latex/embrac/embrac_kerning_test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
