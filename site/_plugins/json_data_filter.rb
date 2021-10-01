# frozen_string_literal: true

module Jekyll
  # Filter to ensure string input is valid as a json string value
  module JSONDataFilter
    def json_value(input)
      input.encode('utf-8', 'binary', undef: :replace)
           .to_json
           .delete_prefix('"')
           .delete_suffix('"')
           .gsub(%r{</?[^>]*>}, '')
    end
  end
end

Liquid::Template.register_filter(Jekyll::JSONDataFilter)
