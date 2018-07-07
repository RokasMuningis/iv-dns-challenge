# LetsEncrypt DNS challenge pre-hook for iv.lt

## Usage (assuming you have certbot)
1. Create config file `cp config.yml.example config.yml`
2. Edit settings
3. Run `sudo ./certbot-auto certonly --manual --manual-auth-hook /pat/to/file/authenticator.sh  --preferred-challenges dns-01 -d *.domain.tld --server https://acme-v02.api.letsencrypt.org/directory`