# mitmproxy Ulauncher Extension

> Manages [mitmproxy](https://mitmproxy.org/)/mitmweb directly from Ulauncher.

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-mitmproxy/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-mitmproxy/workflows)
[![License](https://img.shields.io/github/license/brpaz/ulauncher-mitmproxy.svg?style=for-the-badge)](https://github.com/brpaz/ulauncher-mitmproxy/blob/master/LICENSE)


## Demo

![Extension demo](demo.gif)

## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher)
* Python >= 3
* [mitmproxy](https://mitmproxy.org/)

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-mitmproxy
```

## Usage

Type `mitm` in Ulauncher search input, to access the extension.

Starting the proxy will automatically override any system level proxy configuration that you might have on your system, so you can start using the proxy right away. If you want to disable this behavior and only start the `mitmweb` you can uncheck the `configure system proxy` option on the extension preferences.


### Preferences

- Proxy port and Web Port can be configured on the Extension preferences.


## Development

```
git clone https://github.com/brpaz/ulauncher-mitmproxy
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)

Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee"
style="height: auto !important;width: auto !important;" ></a>

---
## License

MIT &copy; Bruno Paz
