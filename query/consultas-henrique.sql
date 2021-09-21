--totalizacao consumo
select 
  k.* 
from 
  (
    SELECT 
      [nome], 
      [sala], 
      [setor], 
      [andar], 
      [ipv4], 
      max(
        cast([total_impressao] as int)
      )- min(
        cast([total_impressao] as int)
      ) as [total_impressao] 
    FROM 
      [imp-cgdf].[dbo].[impressoras] 
    where 
      [total_impressao] not like 'ERRO' 
    group by 
      [nome], 
      [sala], 
      [setor], 
      [andar], 
      [ipv4]
  ) k 
order by 
  k.[total_impressao] desc

--totalizacao on line e off line
select dt, 'off' as conexao, sum(1) as qtd from [imp-cgdf].[dbo].[impressoras] 
where [total_impressao] like 'ERRO' group by dt
union all
select dt, 'on' as conexao, sum(1) as qtd from [imp-cgdf].[dbo].[impressoras] 
where [total_impressao] not like 'ERRO' group by dt


 