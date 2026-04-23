import { useMutation } from "@tanstack/react-query";
import { analyzeProperty } from "../api/propertyApi";

export function usePropertyAnalysis() {
  return useMutation({
    mutationFn: analyzeProperty,
  });
}
