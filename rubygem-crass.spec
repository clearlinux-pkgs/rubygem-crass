#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-crass
Version  : 1.0.2
Release  : 14
URL      : https://rubygems.org/downloads/crass-1.0.2.gem
Source0  : https://rubygems.org/downloads/crass-1.0.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
Crass
=====
Crass is a Ruby CSS parser that's fully compliant with the
[CSS Syntax Level 3][css] specification.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n crass-1.0.2
gem spec %{SOURCE0} -l --ruby > rubygem-crass.gemspec

%build
gem build rubygem-crass.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
crass-1.0.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/crass-1.0.2
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/crass-1.0.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/crass.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/lib/crass.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/lib/crass/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/lib/crass/scanner.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/lib/crass/token-scanner.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/lib/crass/tokenizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/lib/crass/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/An+B.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/README.rst
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/color3.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/color3_hsl.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/color3_keywords.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/component_value_list.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/declaration_list.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/make_color3_hsl.py
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/make_color3_hsl.pyc
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/make_color3_hsl.pyo
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/make_color3_keywords.py
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/make_color3_keywords.pyc
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/make_color3_keywords.pyo
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/one_component_value.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/one_declaration.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/one_rule.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/rule_list.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/stylesheet.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/css-parsing-tests/stylesheet_bytes.json
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/shared/parse_rules.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/support/common.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/support/serialization/animate.css
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/support/serialization/bootstrap-theme.css
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/support/serialization/bootstrap.css
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/support/serialization/html5-boilerplate.css
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/support/serialization/misc.css
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/support/serialization/pure.css
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/test_crass.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/test_css_parsing_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/test_parse_properties.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/test_parse_rules.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/test_parse_stylesheet.rb
/usr/lib64/ruby/gems/2.3.0/gems/crass-1.0.2/test/test_serialization.rb
/usr/lib64/ruby/gems/2.3.0/specifications/crass-1.0.2.gemspec
