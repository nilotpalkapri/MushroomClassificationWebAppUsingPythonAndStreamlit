mkdir -p ~/.streamlit/
echo "\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credetionals.tonl
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
