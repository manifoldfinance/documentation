import { useRouter } from "next/router";

const Logo = ({ height }) => (
  <svg width="140" height="140"  viewBox="0 0 291 69" fill="none">
</svg>
);


const TITLE_WITH_TRANSLATIONS = {
  "en-US": "Scaling Decentralized Finance"
};

export default {
  github: "https://github.com/manifoldfinance/documentation",
  docsRepositoryBase: "https://github.com/manifoldfinance/documentation/blob/master/pages",
  titleSuffix: " – Manifold Finance",
  search: true,
  unstable_stork: true,
  logo: () => {
    const { locale } = useRouter();
    return (
      <>
        <Logo height={18} />
        <span className="mx-2 font-extrabold hidden md:inline select-none">
          Manifold Finance
        </span>
        <span className="text-gray-600 font-normal hidden lg:!inline whitespace-no-wrap">
          {TITLE_WITH_TRANSLATIONS[locale]}
        </span>
      </>
    );
  },
  head: (
    <>
      {/* Favicons, meta */}
      <link
        rel="apple-touch-icon"
        sizes="180x180"
        href="/favicon/apple-touch-icon.png"
      />
      <link
        rel="icon"
        type="image/png"
        sizes="32x32"
        href="/favicon/favicon-32x32.png"
      />
      <link
        rel="icon"
        type="image/png"
        sizes="16x16"
        href="/favicon/favicon-16x16.png"
      />
      <link rel="manifest" href="/favicon/site.webmanifest" />
      <link
        rel="mask-icon"
        href="/favicon/safari-pinned-tab.svg"
        color="#000000"
      />
      <meta name="msapplication-TileColor" content="#ffffff" />
      <meta name="theme-color" content="#ffffff" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta httpEquiv="Content-Language" content="en" />
      <meta
        name="description"
        content="Scaling Decentralized Finance"
      />
      <meta
        name="og:description"
        content="Scaling Decentralized Finance"
      />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:site" content="@foldfinance" />
      <meta
        name="twitter:image"
        content="https://pbs.twimg.com/profile_images/1389765714551189504/UO8fuMRI_400x400.jpg"
      />
      <meta name="og:title" content="Manifold Finance Documentation" />
      <meta name="og:url" content="https://docs.manifoldfinance.com" />
      <meta
        name="og:image"
        content="https://pbs.twimg.com/profile_images/1389765714551189504/UO8fuMRI_400x400.jpg"
      />
      <meta name="apple-mobile-web-app-title" content="Manifold Finance Documentation" />
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css"
        media="print"
        onLoad="this.media='all'"
      />
    </>
  ),
  footerEditLink: ({ locale }) => {
    switch (locale) {
      case "zh-CN":
        return "在 GitHub 上编辑本页";
      case "es-ES":
        return "Edite esta página en GitHub";
      case "ja":
        return "Github で編集する";
      default:
        return "Edit this page on GitHub";
    }
  },
  footerText: ({ locale }) => {
    switch (locale) {
      case "zh-CN":
        return (
          <a
            href="https://manifoldfinance.com/?utm_source=swr_zh-cn"
            target="_blank"
            rel="noopener"
            className="inline-flex items-center no-underline text-current font-semibold"
          >
            <span className="mr-2">由</span>
            <span className="mr-2">
              <manifoldfinance />
            </span>
            驱动
          </a>
        );
      case "es-ES":
        return (
          <a
            href="https://manifoldfinance.com/?utm_source=swr_es-es"
            target="_blank"
            rel="noopener"
            className="inline-flex items-center no-underline text-current font-semibold"
          >
            <span className="mr-2">Desarrollado por</span>
            <span className="mr-2">
              <manifoldfinance />
            </span>
          </a>
        );
      case "ja":
        return (
          <a
            href="https://manifoldfinance.com/?utm_source=swr_ja"
            target="_blank"
            rel="noopener"
            className="inline-flex items-center no-underline text-current font-semibold"
          >
            <span className="mr-2">提供</span>
            <span className="mr-2">
              <manifoldfinance />
            </span>
          </a>
        );
      default:
        return (
          <a
            href="https://manifoldfinance.com/?utm_source=swr"
            target="_blank"
            rel="noopener"
            className="inline-flex items-center no-underline text-current font-semibold"
          >
            <span className="mr-1">Powered by</span>Ethereum
            <span>
              <manifoldfinance />
            </span>
          </a>
        );
    }
  },
  i18n: [
    { locale: "en-US", text: "English" },
    { locale: "es-ES", text: "Español" },
    { locale: "zh-CN", text: "简体中文" },
    { locale: "ja", text: "日本語" },
  ],
};
