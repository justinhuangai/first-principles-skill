# Example: Product Cost Breakdown

## User Prompt

Our product charges $49 per month, but margins keep shrinking. Use first principles to analyze it.

## Good Response Shape

1. Define the unit: per paying user per month
2. Break cost into hosting, model/API, customer support, payment fees, onboarding labor, churn recovery
3. Mark which costs are irreducible and which are artifacts of product design
4. Identify assumptions:
   - users need all current features
   - every workflow requires real-time processing
   - support must be human-first
5. Propose a zero-based redesign:
   - kill low-value features
   - batch or cache expensive calls
   - move support toward self-serve for repeated issues
6. Suggest one experiment:
   - remove one expensive low-usage feature for a small cohort and observe retention
