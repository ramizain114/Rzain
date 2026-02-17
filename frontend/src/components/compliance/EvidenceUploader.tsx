import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { Upload, File, X } from 'lucide-react'

interface EvidenceUploaderProps {
  controlId: string
  onSuccess: () => void
}

export default function EvidenceUploader({ controlId, onSuccess }: EvidenceUploaderProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'
  const [file, setFile] = useState<File | null>(null)
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [uploading, setUploading] = useState(false)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0])
      if (!title) {
        setTitle(e.target.files[0].name)
      }
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!file) return

    setUploading(true)

    try {
      const formData = new FormData()
      formData.append('file', file)
      formData.append('control_id', controlId)
      formData.append('title', title)
      formData.append('description', description)

      // This would be an API call
      // await uploadEvidence(formData)
      
      onSuccess()
      setFile(null)
      setTitle('')
      setDescription('')
    } catch (error) {
      console.error('Upload failed:', error)
    } finally {
      setUploading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium mb-2">
          {isArabic ? 'العنوان' : 'Title'}
        </label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium mb-2">
          {isArabic ? 'الوصف' : 'Description'}
        </label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm"
          rows={3}
        />
      </div>

      <div>
        <label className="block text-sm font-medium mb-2">
          {isArabic ? 'الملف' : 'File'}
        </label>
        
        {!file ? (
          <label className="flex flex-col items-center justify-center w-full h-32 border-2 border-dashed rounded-lg cursor-pointer hover:bg-accent transition-colors">
            <div className="flex flex-col items-center justify-center pt-5 pb-6">
              <Upload className="w-8 h-8 mb-2 text-muted-foreground" />
              <p className="text-sm text-muted-foreground">
                {isArabic ? 'انقر لتحميل ملف أو اسحب وأفلت' : 'Click to upload or drag and drop'}
              </p>
              <p className="text-xs text-muted-foreground mt-1">
                {isArabic ? 'PDF، Word، Excel، الصور (بحد أقصى 50 ميجابايت)' : 'PDF, Word, Excel, Images (Max 50MB)'}
              </p>
            </div>
            <input
              type="file"
              className="hidden"
              onChange={handleFileChange}
              accept=".pdf,.doc,.docx,.xls,.xlsx,.jpg,.jpeg,.png"
            />
          </label>
        ) : (
          <div className="flex items-center justify-between p-4 border rounded-lg">
            <div className="flex items-center gap-2">
              <File className="w-5 h-5 text-primary" />
              <div>
                <p className="text-sm font-medium">{file.name}</p>
                <p className="text-xs text-muted-foreground">
                  {(file.size / 1024 / 1024).toFixed(2)} MB
                </p>
              </div>
            </div>
            <button
              type="button"
              onClick={() => setFile(null)}
              className="p-1 hover:bg-destructive/10 rounded"
            >
              <X className="w-4 h-4 text-destructive" />
            </button>
          </div>
        )}
      </div>

      <button
        type="submit"
        disabled={!file || uploading}
        className="w-full rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 disabled:opacity-50"
      >
        {uploading ? t('common.loading') : isArabic ? 'رفع الدليل' : 'Upload Evidence'}
      </button>
    </form>
  )
}
