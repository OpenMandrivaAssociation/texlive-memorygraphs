Name:		texlive-memorygraphs
Version:	49631
Release:	2
Summary:	TikZ styles to typeset graphs of program memory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/memorygraphs
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memorygraphs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memorygraphs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines some TikZ styles and adds anchors to
existing styles that ease the declaration of "memory graphs".
It is intended for graphs that represent the memory of a
computer program during its execution.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/memorygraphs
%doc %{_texmfdistdir}/doc/latex/memorygraphs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
