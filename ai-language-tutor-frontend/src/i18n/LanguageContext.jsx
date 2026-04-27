import { createContext, useContext, useState } from "react";
import { translations } from "./translations";

const LanguageContext = createContext(null);

export function LanguageProvider({ children }) {
  const [lang, setLang] = useState("hu");
  const t = translations[lang];
  const toggle = () => setLang(l => l === "hu" ? "en" : "hu");

  return (
    <LanguageContext.Provider value={{ t, lang, toggle }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  return useContext(LanguageContext);
}
