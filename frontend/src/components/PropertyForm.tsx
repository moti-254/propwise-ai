import { useState } from "react";
import {
  Home,
  MapPin,
  BedDouble,
  DollarSign,
  Building2,
  Sparkles,
  AlertCircle,
} from "lucide-react";

interface PropertyFormProps {
  onSubmit: (payload: any) => Promise<void>;
}

export default function PropertyForm({ onSubmit }: PropertyFormProps) {
  const [form, setForm] = useState({
    price: "",
    expected_rent: "",
    location: "",
    property_type: "apartment",
    bedrooms: "",
  });

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const validateForm = () => {
    if (!form.price || Number(form.price) <= 0) {
      return "Please enter a valid property price.";
    }

    if (!form.expected_rent || Number(form.expected_rent) <= 0) {
      return "Please enter a valid monthly rent.";
    }

    if (!form.location.trim()) {
      return "Please provide a location.";
    }

    if (Number(form.expected_rent) > Number(form.price)) {
      return "Monthly rent looks unusually high compared to property price.";
    }

    return null;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    setError("");

    const validationError = validateForm();

    if (validationError) {
      setError(validationError);
      return;
    }

    setLoading(true);

    try {
      await onSubmit({
        price: Number(form.price),
        expected_rent: Number(form.expected_rent),
        location: form.location,
        property_type: form.property_type,
        bedrooms: form.bedrooms ? Number(form.bedrooms) : undefined,
      });
    } catch (err: any) {
      setError(err?.message || "Failed to analyze property.");
    } finally {
      setLoading(false);
    }
  };

  const updateField = (field: string, value: string) => {
    setForm((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  return (
    <div className="relative overflow-hidden rounded-[32px] border border-white/20 bg-white/80 backdrop-blur-xl shadow-[0_20px_80px_rgba(0,0,0,0.08)]">
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-50 via-white to-cyan-50 opacity-90" />

      <div className="relative z-10 p-8 md:p-10">
        <div className="mb-8 flex items-start justify-between gap-6 flex-col md:flex-row">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full bg-indigo-100 px-4 py-2 text-sm font-medium text-indigo-700 mb-4">
              <Sparkles className="h-4 w-4" />
              AI Property Analysis
            </div>

            <h2 className="text-3xl md:text-4xl font-bold tracking-tight text-slate-900">
              Analyze Investment Property
            </h2>

            <p className="mt-3 text-slate-500 max-w-2xl leading-relaxed">
              Get AI-powered investment insights, ROI analysis, market comparison,
              and risk evaluation for your property.
            </p>
          </div>

          <div className="rounded-2xl bg-slate-900 px-5 py-4 text-white shadow-lg">
            <p className="text-xs uppercase tracking-widest text-slate-400">
              Powered by
            </p>
            <p className="mt-1 text-lg font-semibold">Propwise Intelligence</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <InputField
              icon={<DollarSign className="h-5 w-5" />}
              label="Property Price"
              placeholder="e.g. 12,500,000"
              value={form.price}
              onChange={(value) => updateField("price", value)}
              type="number"
            />

            <InputField
              icon={<DollarSign className="h-5 w-5" />}
              label="Expected Monthly Rent"
              placeholder="e.g. 120,000"
              value={form.expected_rent}
              onChange={(value) => updateField("expected_rent", value)}
              type="number"
            />

            <InputField
              icon={<MapPin className="h-5 w-5" />}
              label="Location"
              placeholder="e.g. Nairobi, Westlands"
              value={form.location}
              onChange={(value) => updateField("location", value)}
            />

            <div>
              <label className="mb-2 block text-sm font-semibold text-slate-700">
                Property Type
              </label>

              <div className="relative">
                <Building2 className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-slate-400" />

                <select
                  value={form.property_type}
                  onChange={(e) => updateField("property_type", e.target.value)}
                  className="w-full rounded-2xl border border-slate-200 bg-white py-4 pl-12 pr-4 text-slate-900 shadow-sm transition-all outline-none focus:border-indigo-500 focus:ring-4 focus:ring-indigo-100"
                >
                  <option value="apartment">Apartment</option>
                  <option value="house">House</option>
                  <option value="villa">Villa</option>
                  <option value="commercial">Commercial</option>
                  <option value="land">Land</option>
                </select>
              </div>
            </div>

            <InputField
              icon={<BedDouble className="h-5 w-5" />}
              label="Bedrooms (Optional)"
              placeholder="e.g. 3"
              value={form.bedrooms}
              onChange={(value) => updateField("bedrooms", value)}
              type="number"
            />
          </div>

          {error && (
            <div className="flex items-start gap-3 rounded-2xl border border-red-200 bg-red-50 px-4 py-4 text-red-700 animate-in fade-in slide-in-from-top-2 duration-300">
              <AlertCircle className="h-5 w-5 mt-0.5" />
              <p className="text-sm font-medium">{error}</p>
            </div>
          )}

          <div className="flex flex-col md:flex-row items-center justify-between gap-6 border-t border-slate-200 pt-8">
            <div className="flex items-center gap-3 text-sm text-slate-500">
              <Home className="h-4 w-4" />
              Real-time AI investment scoring & market analysis
            </div>

            <button
              type="submit"
              disabled={loading}
              className="group relative inline-flex items-center justify-center overflow-hidden rounded-2xl bg-slate-900 px-8 py-4 font-semibold text-white transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl hover:shadow-indigo-500/20 disabled:opacity-60 disabled:cursor-not-allowed"
            >
              <span className="absolute inset-0 bg-gradient-to-r from-indigo-600 via-violet-600 to-cyan-600 opacity-0 transition-opacity duration-300 group-hover:opacity-100" />

              <span className="relative flex items-center gap-2">
                {loading ? (
                  <>
                    <div className="h-5 w-5 animate-spin rounded-full border-2 border-white/30 border-t-white" />
                    Analyzing Property...
                  </>
                ) : (
                  <>
                    <Sparkles className="h-5 w-5" />
                    Analyze Property
                  </>
                )}
              </span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

interface InputFieldProps {
  icon: React.ReactNode;
  label: string;
  placeholder: string;
  value: string;
  onChange: (value: string) => void;
  type?: string;
}

function InputField({
  icon,
  label,
  placeholder,
  value,
  onChange,
  type = "text",
}: InputFieldProps) {
  return (
    <div>
      <label className="mb-2 block text-sm font-semibold text-slate-700">
        {label}
      </label>

      <div className="relative group">
        <div className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 group-focus-within:text-indigo-600 transition-colors">
          {icon}
        </div>

        <input
          type={type}
          placeholder={placeholder}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          className="w-full rounded-2xl border border-slate-200 bg-white py-4 pl-12 pr-4 text-slate-900 shadow-sm transition-all outline-none focus:border-indigo-500 focus:ring-4 focus:ring-indigo-100"
        />
      </div>
    </div>
  );
}
