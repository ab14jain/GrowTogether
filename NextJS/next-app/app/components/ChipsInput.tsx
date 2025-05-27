'use client';
import React, { useState } from "react";

function ChipsInput() {
    const [chips, setChips] = useState<string[]>([]);

    return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", margin: "40px 0" }}>
            <h2>Chips Input</h2>
            <input
                type="text"
                placeholder="Type a chip and press tag"
                style={{ padding: "8px", width: "200px" }}
                onKeyDown={(e) => {
                    const input = e.target as HTMLInputElement;
                    //input.value = ""; // Clear the input when clicked
                    
                    if (e.key == 'Enter') { //Enter keycode
                        e.preventDefault(); // Prevent form submission
                        const value = input.value.trim();
                        if (value && !chips.includes(value)) {
                            setChips([...chips, value]);
                            input.value = ""; // Clear the input after adding the chip
                        }
                    }
                }}
            />

            <p> 
                <ul>
                {/* {chips.forEach(ch => return {<li>ch</li>})} */}
                {chips.map((chip, index) => (
                    <li key={index} style={{ display: "inline-block", margin: "5px", padding: "5px 10px", backgroundColor: "#e0e0e0", borderRadius: "16px" }}>
                        {chip}
                        <button
                            onClick={() => setChips(chips.filter((c) => c !== chip))}
                            style={{ marginLeft: "8px", cursor: "pointer" }}
                        >
                            x
                        </button>
                    </li>
                ))}
                </ul>
                
            </p>
        </div>
    );
}

export default ChipsInput;