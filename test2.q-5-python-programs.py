def calculate_ticket_price(seats, timing, is_weekend):
    
    # 1. Base prices
    prices = {
        "VIP": 500,
        "REGULAR": 300,
        "ECONOMY": 150
    }
    
    # 2. Timing multipliers
    timing_multiplier = {
        "morning": 0.8,
        "afternoon": 1,
        "evening": 1.2,
        "night": 1.5
    }
    
    # 9. Ignore invalid seat types
    valid_seats = [seat for seat in seats if seat in prices]
    
    # 10. If no valid seats
    if len(valid_seats) == 0:
        return "No valid booking"
    
    # 1. Base total
    base_total = sum(prices[seat] for seat in valid_seats)
    
    # 2. Timing adjustment
    timing_adjustment = base_total * timing_multiplier.get(timing, 1)
    
    # 3. Weekend surcharge (+10%)
    total = timing_adjustment
    if is_weekend:
        total += total * 0.10
    
    # 4. Bulk discount (≥ 5 seats)
    discount = 0
    if len(valid_seats) >= 5:
        discount = total * 0.15
        total -= discount
    
    # 5. Booking fee
    booking_fee = 50 * len(valid_seats)
    total += booking_fee
    
    # 6. GST (12%)
    tax = total * 0.12
    
    # 7. Final amount
    final_amount = total + tax
    
    # 8. Return result (rounded)
    return {
        "base_total": round(base_total),
        "timing_adjustment": round(timing_adjustment),
        "discount": round(discount),
        "tax": round(tax),
        "final_amount": round(final_amount)
    }
seats = ["VIP", "REGULAR", "VIP"]
timing = "evening"
is_weekend = True

result = calculate_ticket_price(seats, timing, is_weekend)
print(result)