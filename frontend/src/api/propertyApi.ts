import axios from "axios";

export const api = axios.create({
  baseURL:process.env.NEXT_PUBLIC_API_URL || "https://localhost:8000/api/v1",
});

export async function analyzeProperty(payload: any) {
  const response = await api.post("/property/analyze", payload);
  return response.data;
}
