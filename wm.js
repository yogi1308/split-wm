(function scrapeWalmartJSONOnly() {
    let items = [];
    let tax = 0;

    // 1. Extract Items
    let itemRows = document.querySelectorAll('[data-testid="itemtile-stack"]');

    itemRows.forEach(row => {
        let nameEl = row.querySelector('[data-testid="productName"]');
        let name = nameEl ? nameEl.innerText.trim() : "Unknown Item";

        let priceEl = row.querySelector('[data-testid="line-price"]');
        let priceText = priceEl ? priceEl.innerText : "0";
        let price = parseFloat(priceText.replace(/[^0-9.]/g, ''));

        let qtyEl = row.querySelector('.bill-item-quantity');
        let qtyText = qtyEl ? qtyEl.innerText : "Qty 1";
        let qtyMatch = qtyText.match(/Qty\s?(\d+)/i);
        let qty = qtyMatch ? parseInt(qtyMatch[1]) : 1;

        if (name !== "Unknown Item") {
            items.push({
                item: name,
                price: price,
                qty: qty
            });
        }
    });

    // 2. Extract Tax
    const potentialTaxRows = document.querySelectorAll('.flex.justify-between, [class*="payment-group"], .print-fees-item');
    potentialTaxRows.forEach(row => {
        const text = row.innerText.replace(/\n/g, ' ').trim();
        if (text.startsWith("Tax") && text.match(/\$[0-9,]+\.[0-9]{2}/)) {
            const priceMatch = text.match(/\$[0-9,]+\.[0-9]{2}/);
            if (priceMatch) {
                tax = parseFloat(priceMatch[0].replace(/[^0-9.]/g, ''));
            }
        }
    });

    // 3. Output Pure JSON
    const output = {
        items: items,
        tax: tax
    };

    console.clear();
    console.log(JSON.stringify(output, null, 2));

    // Optional: Automatically copy to clipboard (works in Chrome/Edge console)
    if (typeof copy === 'function') {
        copy(output);
        console.log("%cJSON copied to clipboard!", "color: gray; font-style: italic;");
    }
})();
