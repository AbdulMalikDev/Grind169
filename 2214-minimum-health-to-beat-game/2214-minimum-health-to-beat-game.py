class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        numSum = sum(damage)
        
        minHealth = sys.maxsize
        
        for num in damage:
            healthAfterArmor  = num - min(armor,num)
            
            currMinHealth = healthAfterArmor + (numSum - num) + 1
            minHealth = min(minHealth,currMinHealth)
            
        return minHealth
        