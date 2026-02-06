# Azure OpenAI Prompts for Cupid's Command Center

This file contains all the prompt templates used by the AI Copilot and Power Automate flows.

---

## System Prompt (Main Bot)

```
You are Cupid's AI Copilot, an intelligent assistant for the Cupid Chocolate Company's Command Center. You help operations managers monitor Valentine's Day activities, identify risks, and take action to ensure customer satisfaction.

Your personality:
- Helpful and proactive
- Slightly romantic/playful (it's Valentine's Day!)
- Data-driven and precise
- Urgent when there are critical issues

You have access to:
- Real-time sales data across all regions
- Supply chain status and inventory levels
- Customer sentiment and delivery performance
- Historical trends and predictions

When responding:
1. Always provide specific numbers and metrics
2. Prioritize critical issues (stock-outs, delays)
3. Offer actionable recommendations
4. Use emojis sparingly for visual clarity

Current date/time context: {{current_datetime}}
```

---

## Risk Assessment Prompt

```
Analyze the following operational data and provide a risk assessment:

INVENTORY DATA:
{{inventory_summary}}

DELIVERY STATUS:
{{delivery_metrics}}

SALES VELOCITY:
{{sales_velocity}}

WEATHER CONDITIONS:
{{weather_data}}

Please identify:
1. TOP 3 CRITICAL RISKS (immediate action needed)
2. TOP 3 WARNING ITEMS (monitor closely)
3. RECOMMENDED ACTIONS for each risk

Format your response with clear headers and bullet points. Include specific numbers and timeframes.
```

---

## Customer Email Generation Prompt

```
Write a customer notification email for a delayed Valentine's Day order.

CUSTOMER INFO:
- Name: {{customer_name}}
- Order Number: {{order_id}}
- Original Delivery Date: {{original_date}}
- New Delivery Date: {{new_date}}
- Delay Reason: {{delay_reason}}
- Products: {{product_list}}

TONE: Warm, apologetic, but reassuring
LENGTH: 150-200 words
INCLUDE: 
- Sincere apology
- Clear explanation (without blame)
- New delivery timeline
- Discount code: CUPIDCARES (15% off)
- Contact info for questions

Make it feel personal and Valentine's themed without being too cheesy.
```

---

## Sales Summary Prompt

```
Based on the following sales data, provide an executive summary:

TODAY'S SALES:
{{todays_sales}}

COMPARISON:
- Yesterday: {{yesterday_total}}
- Same day last year: {{last_year_total}}
- Target: {{daily_target}}

TOP PRODUCTS:
{{top_products}}

REGIONAL BREAKDOWN:
{{regional_data}}

Provide:
1. 3 key highlights (positive trends)
2. 1-2 areas of concern
3. One actionable recommendation

Keep the tone upbeat but professional. Use 💝📊📈 emojis sparingly.
```

---

## Recovery Plan Generation Prompt

```
Create a recovery plan for the following operational issue:

ISSUE TYPE: {{issue_type}}
SEVERITY: {{severity}}
AFFECTED: {{affected_count}} orders/customers
REGION: {{region}}
ROOT CAUSE: {{root_cause}}

AVAILABLE RESOURCES:
- Alternative suppliers: {{alt_suppliers}}
- Backup warehouses: {{backup_warehouses}}
- Budget for remediation: {{budget}}

Generate a detailed recovery plan with:

1. IMMEDIATE ACTIONS (next 2 hours)
   - List specific steps with owners
   
2. SHORT-TERM ACTIONS (today)
   - Mitigation steps
   
3. CUSTOMER COMMUNICATION
   - Draft message template
   
4. PREVENTION MEASURES
   - How to avoid this in the future

Include estimated time and cost for each action.
```

---

## Inventory Forecast Prompt

```
Analyze inventory levels and predict stockout risks:

CURRENT INVENTORY:
{{inventory_data}}

SALES VELOCITY (last 24 hours):
{{velocity_data}}

INCOMING SHIPMENTS:
{{incoming_shipments}}

HISTORICAL PATTERNS:
- Valentine's Day typically sees {{peak_multiplier}}x normal sales
- Peak hours: {{peak_hours}}

For each product, calculate:
1. Hours until stockout at current velocity
2. Risk level (Critical/Warning/OK)
3. Recommended reorder quantity
4. Priority ranking

Format as a table and highlight anything under 12 hours remaining.
```

---

## Daily Summary Generation Prompt

```
Generate a daily operations summary for leadership:

KEY METRICS:
{{metrics_json}}

INCIDENTS:
{{incidents_list}}

CUSTOMER FEEDBACK:
{{feedback_summary}}

Create an executive summary with:

1. HEADLINE (one sentence capturing the day)
2. TOP 3 WINS 🏆
3. TOP 3 CHALLENGES ⚠️
4. TOMORROW'S FOCUS 🎯
5. KEY NUMBERS (bullet points)

Keep it under 300 words. Make it scannable for busy executives.
End with a Valentine's Day themed motivational note.
```

---

## Escalation Decision Prompt

```
Evaluate if this issue requires human escalation:

ISSUE: {{issue_description}}
DATA POINTS: {{relevant_data}}
AI CONFIDENCE: {{confidence_score}}%
ATTEMPTED ACTIONS: {{previous_actions}}

Criteria for escalation:
- Financial impact > €10,000
- Customer impact > 100 orders
- Safety/legal concerns
- AI confidence < 70%
- Issue persists after 2 automated attempts

RESPOND WITH:
{
  "escalate": true/false,
  "reason": "explanation",
  "urgency": "critical/high/medium/low",
  "recommended_escalation_path": "who should handle this",
  "context_for_human": "brief summary for the human reviewer"
}
```

---

## Configuration

```json
{
  "model": "gpt-4",
  "temperature": 0.7,
  "max_tokens": 1000,
  "top_p": 0.95,
  "frequency_penalty": 0.3,
  "presence_penalty": 0.3,
  "stop_sequences": ["---", "END"]
}
```

---

## Usage Notes

1. **Always include current datetime** in the system prompt for time-sensitive operations
2. **Sanitize customer PII** before sending to Azure OpenAI
3. **Log all prompts and responses** for audit trail
4. **Set appropriate content filters** for customer-facing responses
5. **Use streaming** for real-time dashboard updates

---

*Last updated: February 2026*
