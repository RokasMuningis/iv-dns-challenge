# LetsEncrypt DNS challenge pre-hook for iv.lt

## Must know
As IV's endpoint replaces ALL dns records, you've to edit config.yml to include all your current records. Ideally, it could retrieve data and just append it.

## Usage (assuming you have certbot)
1. Create config file `cp config.json.example config.json`
2. Edit settings
3. Run `sudo ./certbot-auto certonly --manual --manual-auth-hook /pat/to/file/authenticator.shs  --preferred-challenges dns-01 -d *.domain.tld --server https://acme-v02.api.letsencrypt.org/directory`