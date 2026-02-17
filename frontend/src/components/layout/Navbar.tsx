import { useTranslation } from 'react-i18next'
import { useAuthStore } from '../../stores/auth-store'
import { useUIStore } from '../../stores/ui-store'
import { LogOut, Globe } from 'lucide-react'

export default function Navbar() {
  const { t, i18n } = useTranslation()
  const { user, logout } = useAuthStore()
  const { language, setLanguage } = useUIStore()

  const toggleLanguage = () => {
    const newLang = language === 'en' ? 'ar' : 'en'
    setLanguage(newLang)
    i18n.changeLanguage(newLang)
  }

  return (
    <header className="flex h-16 items-center justify-between border-b bg-card px-6">
      <div className="flex items-center gap-4">
        <h2 className="text-lg font-semibold">
          {user?.full_name_en || user?.username}
        </h2>
      </div>

      <div className="flex items-center gap-4">
        <button
          onClick={toggleLanguage}
          className="flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium transition-colors hover:bg-accent"
        >
          <Globe className="h-4 w-4" />
          {language === 'en' ? 'العربية' : 'English'}
        </button>

        <button
          onClick={logout}
          className="flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium transition-colors hover:bg-destructive hover:text-destructive-foreground"
        >
          <LogOut className="h-4 w-4" />
          {t('auth.logout')}
        </button>
      </div>
    </header>
  )
}
